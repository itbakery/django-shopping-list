from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', 'shopping_list.views.home'),
    url(r'^login/$', 'shopping_list.views.login'),
    url(r'^logout/$', 'shopping_list.views.logout'),
    url(r'^auth/$', 'shopping_list.views.auth_view'),
    url(r'^signup/$', 'shopping_list.views.signup'),
    url(r'^shopping_list/$', 'shopping_list.views.shopping_list'),
    url(r'^add_item/$', 'shopping_list.views.add_item'),
    url(r'^invalid/$', 'shopping_list.views.invalid_login'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   url(r'^admin/', include(admin.site.urls)),
)
