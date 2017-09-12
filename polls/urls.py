from django.conf.urls import url
from polls import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
]
