from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zeromq.views.home', name='home'),
    # url(r'^zeromq/', include('zeromq.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('node.views',
    (r'^$', 'view_home_page', {'home_page_template': 'node/home_page.html'}, 'home_page'),
    (r'^create/$', 'view_create_node', {'create_node_template': 'node/create_node.html'}, 'create_node'),
    (r'^save/$', 'view_save_node', {}, 'save_node'),
    (r'^start_everything/$', 'view_start_everything', {},'start_everything'),
    (r'^stop_everything/$', 'view_stop_everything', {},'stop_everything'),
    (r'^start_processes/$', 'view_start_processes', {},'start_processes'),
    (r'^stop_processes/$', 'view_stop_processes', {},'stop_processes'),
)
