from django.conf.urls import url
from ipconfig import views

urlpatterns = [
    url(r'^my_ip/$', views.show, name='ipconfig'),
]