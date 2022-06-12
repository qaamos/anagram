import re
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django import forms

from anagram.models import Word
from anagram import logic

# Create your views here.
def index(request):
    return render(request, 'anagram/index.html')

# TODO: sanitize/clean input
def generate(request):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            input = request.POST.get('userinput')
            wordExists = Word.objects.filter(wordText=input).exists()
            if not wordExists:
                word = Word(wordText=input)
                word.save()
            # logic.webRequest(input) TODO: make this work
            return HttpResponseRedirect('/anagram/result/')
    else:
        form = forms.Form()
    return render(request, 'anagram/index.html', {'form' : form})

def result(request):
    return render(request, 'anagram/result.html')
