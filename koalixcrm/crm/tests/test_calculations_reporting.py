from django.test import TestCase
from django.test import LiveServerTestCase
from koalixcrm.crm.models import Project
from koalixcrm.crm.models import ReportingPeriod
from koalixcrm.crm.models import Customer
from koalixcrm.crm.models import CustomerGroup
from koalixcrm.crm.models import CustomerBillingCycle
from koalixcrm.crm.models import Currency
from koalixcrm.crm.models import Task
from koalixcrm.crm.models import TaskStatus
from koalixcrm.djangoUserExtension.models import UserExtension
from koalixcrm.djangoUserExtension.models import TemplateSet
from koalixcrm.crm.models import Work
from koalixcrm.crm.models import EmployeeAssignmentToTask
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime


class ReportingCalculationsTest(TestCase):
    def setUp(self):
        datetime_now=datetime.datetime(2024, 1, 1, 0, 00)
        start_date=(datetime_now - datetime.timedelta(days=30)).date()
        end_date_first_task=(datetime_now + datetime.timedelta(days=30)).date()
        end_date_second_task=(datetime_now + datetime.timedelta(days=60)).date()
        date_now=datetime_now.date()
        test_billing_cycle=CustomerBillingCycle.objects.create(
            name="30 days to pay",
            time_to_payment_date=30,
            payment_reminder_time_to_payment=10
        )
        test_user=User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@admin.com')
        test_customer_group=CustomerGroup.objects.create(
            name="Tripple A"
        )
        test_customer=Customer.objects.create(
            name="John Smith",
            last_modified_by=test_user,
            default_customer_billing_cycle=test_billing_cycle,
        )
        test_customer.is_member_of=[test_customer_group,]
        test_customer.save()
        test_currency=Currency.objects.create(
            description="Swiss Francs",
            short_name="CHF",
            rounding=0.05,
        )
        test_template_set=TemplateSet.objects.create(
            title="Just an empty Template Set"
        )
        UserExtension.objects.create(
            user=test_user,
            default_template_set=test_template_set,
            default_currency=test_currency
        )
        test_project = Project.objects.create(
            project_manager=test_user,
            project_name="This is a test project",
            last_modification=date_now,
            last_modified_by=test_user
        )
        ReportingPeriod.objects.create(
            project=test_project,
            begin=start_date,
            end=end_date_first_task,
            title="This is a Test Period"
        )
        test_task_status = TaskStatus.objects.create(
            title="planned",
            description="This represents the state when something has been planned but not yet started",
            is_done=False
        )
        Task.objects.create(
            title="Test Task",
            planned_start_date=start_date,
            planned_end_date=end_date_first_task,
            project=test_project,
            description="This is a simple test task",
            status=test_task_status,
            last_status_change=date_now
        )
        Task.objects.create(
            title="2nd Test Task",
            planned_start_date=start_date,
            planned_end_date=end_date_second_task,
            project=test_project,
            description="This is an other simple test task",
            status=test_task_status,
            last_status_change=date_now
        )

    def test_calculation_of_reported_hours(self):
        datetime_now = datetime.datetime(2024, 1, 1, 0, 00)
        datetime_later_1 = datetime.datetime(2024, 1, 1, 2, 00)
        datetime_later_2 = datetime.datetime(2024, 1, 1, 3, 30)
        datetime_later_3 = datetime.datetime(2024, 1, 1, 5, 45)
        datetime_later_4 = datetime.datetime(2024, 1, 1, 6, 15)
        date_now = datetime_now.date()
        test_task_first = Task.objects.get(title="Test Task")
        test_task_second = Task.objects.get(title="2nd Test Task")
        test_project = Project.objects.get(project_name="This is a test project")
        self.assertEqual(
            (test_task_first.planned_duration()).__str__(), "60 days, 0:00:00")
        self.assertEqual(
            (test_task_first.planned_effort()).__str__(), "0")
        self.assertEqual(
            (test_task_second.planned_duration()).__str__(), "90 days, 0:00:00")
        self.assertEqual(
            (test_task_second.planned_effort()).__str__(), "0")
        test_user = User.objects.get(username="admin")
        test_reporting_period = ReportingPeriod.objects.get(title="This is a Test Period")
        test_employee = UserExtension.objects.get(user=test_user)
        EmployeeAssignmentToTask.objects.create(
            employee=test_employee,
            planned_effort="2.00",
            task=test_task_first
        )
        EmployeeAssignmentToTask.objects.create(
            employee=test_employee,
            planned_effort="1.50",
            task=test_task_first
        )
        EmployeeAssignmentToTask.objects.create(
            employee=test_employee,
            planned_effort="4.75",
            task=test_task_second
        )
        EmployeeAssignmentToTask.objects.create(
            employee=test_employee,
            planned_effort="3.25",
            task=test_task_second
        )
        self.assertEqual(
            (test_task_first.planned_effort()).__str__(), "3.50")
        self.assertEqual(
            (test_task_first.effective_effort(reporting_period=None)).__str__(), "0.0")
        self.assertEqual(
            (test_task_second.planned_effort()).__str__(), "8.00")
        self.assertEqual(
            (test_task_second.effective_effort(reporting_period=None)).__str__(), "0.0")
        Work.objects.create(
            employee=test_employee,
            date=date_now,
            start_time=datetime_now,
            stop_time=datetime_later_1,
            short_description="Not really relevant",
            description="Performed some hard work",
            task=test_task_first,
            reporting_period=test_reporting_period
        )
        Work.objects.create(
            employee=test_employee,
            date=date_now,
            start_time=datetime_later_1,
            stop_time=datetime_later_2,
            short_description="Not really relevant 2nd part",
            description="Performed some hard work 2nd part",
            task=test_task_first,
            reporting_period=test_reporting_period
        )
        Work.objects.create(
            employee=test_employee,
            date=date_now,
            start_time=datetime_now,
            stop_time=datetime_later_3,
            short_description="Not really relevant",
            description="Performed some hard work",
            task=test_task_second,
            reporting_period=test_reporting_period
        )
        Work.objects.create(
            employee=test_employee,
            date=date_now,
            start_time=datetime_now,
            stop_time=datetime_later_4,
            short_description="Not really relevant 2nd part",
            description="Performed some hard work 2nd part",
            task=test_task_second,
            reporting_period=test_reporting_period
        )
        self.assertEqual(
            (test_task_first.effective_effort(reporting_period=None)).__str__(), "3.5")
        self.assertEqual(
            (test_task_second.effective_effort(reporting_period=None)).__str__(), "12.0")
        self.assertEqual(
            (test_project.effective_effort(reporting_period=None)).__str__(), "15.5")
        self.assertEqual(
            (test_project.planned_effort()).__str__(), "11.50")


class ReportingCalculationsUITest(LiveServerTestCase):

    def setUp(self):
        firefox_options = webdriver.firefox.options.Options()
        firefox_options.set_headless(headless=True)
        self.selenium = webdriver.Firefox(firefox_options=firefox_options)
        prepare_test = ReportingCalculationsTest()
        prepare_test.setUp()

    def tearDown(self):
        self.selenium.quit()

    def test_registration_of_work(self):
        selenium = self.selenium
        # login
        selenium.get('%s%s' % (self.live_server_url, '/koalixcrm/crm/reporting/time_tracking/'))
        # the browser will be redirected to the login page
        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.ID, 'id_username'))
            WebDriverWait(selenium, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        username = selenium.find_element_by_xpath('//*[@id="id_username"]')
        password = selenium.find_element_by_xpath('//*[@id="id_password"]')
        submit_button = selenium.find_element_by_xpath('/html/body/div/article/div/div/form/div/ul/li/input')
        username.send_keys("admin")
        password.send_keys("admin")
        submit_button.send_keys(Keys.RETURN)
        # after the login, the browser is redirected to the target url /koalixcrm/crm/reporting/time_tracking
        try:
            element_present = EC.presence_of_element_located((By.ID, 'id_form-0-projects'))
            WebDriverWait(selenium, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        # find the form element
        project = selenium.find_element_by_xpath('//*[@id="id_form-0-projects"]')
        task = selenium.find_element_by_xpath('//*[@id="id_form-0-task"]')
        date = selenium.find_element_by_xpath('//*[@id="id_form-0-date"]')
        start_time = selenium.find_element_by_xpath('//*[@id="id_form-0-start_time"]')
        stop_time = selenium.find_element_by_xpath('//*[@id="id_form-0-stop_time"]')
        description = selenium.find_element_by_xpath('//*[@id="id_form-0-description"]')
        save = selenium.find_element_by_name('save')