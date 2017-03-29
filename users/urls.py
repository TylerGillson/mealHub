from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user_hub/$', views.UserHubView, name = 'user_hub'),
]
