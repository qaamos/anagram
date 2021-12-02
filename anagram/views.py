from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'anagram/index.html')

def generate(request):
    return HttpResponse('Hello World')

def result(request):
    return render(request, 'anagram/result.html')
