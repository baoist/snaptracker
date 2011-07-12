from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', direct_to_template, {'template': 'index.html'})
    # Examples:
    # url(r'^$', 'snaptracker.views.home', name='home'),
    # url(r'^snaptracker/', include('snaptracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'snapshot.views.home', name='home'),
    url(r'^snapshot/$', 'snapshot.views.snap', name='snap'),
    url(r'^snapshot/complete', 'snapshot.views.complete', name='complete'),
    url(r'^snapshot/listall', 'snapshot.views.listall', name='listall'),
)

urlpatterns += patterns('',
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
      'show_indexes': True}),
)
