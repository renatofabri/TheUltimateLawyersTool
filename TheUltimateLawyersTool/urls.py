from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TheUltimateLawyersTool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'Dashboard.views.home', name='dashboard'),


    #url(r'^admin/', include(admin.site.urls)),
)
