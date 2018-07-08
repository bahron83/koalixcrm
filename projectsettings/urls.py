"""test_koalixcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls.static import *
from django.contrib.staticfiles.urls import static
from django.contrib import admin
from django.conf.urls import include
from filebrowser.sites import site
from rest_framework import routers
from koalixcrm.crm.views.restinterface import TaskAsJSON, ContractAsJSON, TaskStatusAsJSON, ProjectAsJSON

router = routers.DefaultRouter()
router.register(r'tasks', TaskAsJSON)
router.register(r'contracts', ContractAsJSON)
router.register(r'project', ProjectAsJSON)
router.register(r'taskstatus', TaskStatusAsJSON)

admin.autodiscover()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^koalixcrm/crm/reporting/', include('koalixcrm.crm.reporting.urls')), # koalixcrm crm reporting URLS
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

