from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mapper),
    url(r'^$', views.frontpage),
]