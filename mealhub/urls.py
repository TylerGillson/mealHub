from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.register, name = 'register'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),

    url(r'^users/', include('users.urls')),
    url(r'^meals/', include('meals.urls')),
    url(r'^$', views.home, name ='home'),
]
