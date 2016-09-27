from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newForm$', views.new, name='newForm'),
    url(r'^newItem$', views.addItem, name='addItem'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^add/$', views.add_to_wishlist, name='add_to_wishlist'),
    url(r'^remove/(?P<id>\d+)$', views.remove_from_wishlist, name='remove'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^logOut$', views.logOut, name='logOut'),

]
