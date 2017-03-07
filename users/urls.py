from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views



from . import views

urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'users/login.html'}, name ='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'users/login.html'}, name = 'login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/users'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^chefs/$', views.ChefsView, name ='chefs'),
    url(r'^mouths/$', views.MouthsView, name='mouths'),
]