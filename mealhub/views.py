from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to mealHub home page! :)<form action ='/users'><input type ='submit' value=\"login\" /></form>")