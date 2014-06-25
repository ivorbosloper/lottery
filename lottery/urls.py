from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('lottery.views',
    (r'^admin/', include(admin.site.urls)),
    url('^$', 'index', name='index'),
    url('^json/?$', 'jsonf', name='jsonf'),
)
