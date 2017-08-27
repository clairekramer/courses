from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^courses$', views.index, name='home'),
    url(r'^courses/add$', views.add, name='add'),
    url(r'^courses/(?P<id>\d+)/remove$', views.remove, name='remove'),
    url(r'^courses/(?P<id>\d+)/delete$', views.delete, name='delete'),
]
