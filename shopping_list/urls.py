from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'shopping_list.views.home'),
    # url(r'^shopping_list/', include('shopping_list.foo.urls')),
    url(r'^login/$', 'shopping_list.views.login'),
    url(r'^logout/$', 'shopping_list.views.logout'),
    url(r'^auth/$', 'shopping_list.views.auth_view'),
    url(r'^loggedin/$', 'shopping_list.views.loggedin'),
    url(r'^invalid/$', 'shopping_list.views.invalid_login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
)
