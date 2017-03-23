from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^search/$', views.SearchView, name ='search'),
]

#want to create a url pattern like ../user_name/meal_name
