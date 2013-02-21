from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web.views.home', name='home'),
    url(r'^cmd/oa', 'web.views.open_all', name='open_all'),
    url(r'^cmd/ca', 'web.views.close_all', name='close_all'),
    url(r'^cmd/([\w\s]+)?', 'web.views.cmd', name='cmd'),

    # url(r'^x10/', include('x10.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


)
