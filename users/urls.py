from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^chefs/$', views.ChefsView, name ='chefs'),
    url(r'^mouths/$', views.MouthsView, name='mouths'),
]
