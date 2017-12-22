from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.logs, name='logs'),
    url(r'^readlog', views.readlog, name='readlog'),
]
