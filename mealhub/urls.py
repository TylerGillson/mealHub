from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


#for meal photos
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # House-keeping URLs:
    url(r'^admin/', admin.site.urls),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^register/$', views.register, name = 'register'),
    url(r'^about/$', views.aboutUs, name='about'),
    url(r'^user_hub/$', views.UserHubView, name = 'user_hub'),
    url(r'^search/$', views.SearchView, name ='search'),

    url(r'^meals/(?P<username>\w+)\/(?P<mealname>\w+)/', views.meals, name = 'meals'),

    url(r'^$', views.home, name ='home'),
    url(r'^home/$', views.home, name='home'),

    # Postman URLs:
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
