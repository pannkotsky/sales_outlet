"""sales_outlet URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView

from select2 import urls as select2_urls

from documents.views import ShipmentsView

admin.site.site_header = _('Sales Outlet')
admin.site.site_title = _('Sales Outlet')
admin.site.index_title = _('Sales Outlet')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shipments/$', ShipmentsView.as_view(), name='shipments'),
    url(r'^shipments/(?P<product_code>.*)/$', ShipmentsView.as_view(), name='shipments'),
    url(r'^select2/', include(select2_urls, namespace='select2')),
    url(r'^$', RedirectView.as_view(pattern_name='admin:index'))
]
