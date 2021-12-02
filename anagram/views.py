from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'anagram/index.html')

def generate(request):
    return HttpResponse('Hello World')