from django.conf.urls import url
from landing import views

urlpatterns = [
    url(r'^article/(?P<question_id>[0-9]+)/$', views.single, name='single'),
    url(r'^$', views.landing, name='landing'),

]