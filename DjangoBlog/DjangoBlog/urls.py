from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# from blogengine.views import getPosts

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoBlog.views.home', name='home'),
    # url(r'^DjangoBlog/', include('DjangoBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'', 'blogengine.views.getRecentPosts'),
    url(r'^$', 'blogengine.views.getPosts'),
    url(r'^(?P<selected_page>\d+)/?$', 'blogengine.views.getPosts'),
    # Blog posts
    # url(r'^(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPosts'),
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),
)
