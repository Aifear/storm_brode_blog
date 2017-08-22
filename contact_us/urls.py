from django.conf.urls import url
from contact_us import views

urlpatterns = [
    url(r'^contact/', views.contact, name='contact'),
]