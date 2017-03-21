from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.template import loader

def SearchView(request):
    return render(request, 'meals/search.html')
