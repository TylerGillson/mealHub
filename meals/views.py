from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def SearchView(request):
    return render(request, 'meals/search.html')