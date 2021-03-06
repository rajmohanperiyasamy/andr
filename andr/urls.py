from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'andr.views.home', name='home'),
     url(r'^downloads/$', 'andr.views.about', name='about'),
     url(r'^clients/$', 'andr.views.clients', name='clients'),
     url(r'^portfolio/$', 'andr.views.portfolio', name='portfolio'),
     url(r'^contacts/$', 'andr.views.contacts', name='contacts'),
     url(r'^file_download/(?P<pk>\d+)$', 'and.views.file_download',name='file_download'),
#     url(r'^android/', include('android.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
