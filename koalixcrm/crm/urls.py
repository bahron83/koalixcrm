from django.conf.urls import url, include

from koalixcrm.crm import views


urlpatterns = [
    #url(r'^customer_print/?$', views.customer_view, name='customer_print'),
    url(r'^customer_resume/(?P<id>[^/]*)$', views.customer_resume, name="customer_resume"),
]