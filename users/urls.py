from django.conf.urls import url
from mealhub import views as mealhub_views
from . import views

urlpatterns = [
    url(r'^chefs/$', views.ChefsView, name ='chefs'),
    url(r'^mouths/$', views.MouthsView, name='mouths'),
    url(r'^user_hub/$', mealhub_views.user_hub, name = 'user_hub'),
]
