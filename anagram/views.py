import re
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django import forms

from anagram.models import Word
from anagram import logic

def index(request):
    return render(request, 'anagram/index.html')

# TODO: sanitize/clean input
def generate(request):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            input = request.POST.get('userinput')
            anagrams = logic.webRequest(input)
            print(anagrams)
            # TODO: also save anagrams for words
            for anagram in anagrams:
                wordExists = Word.objects.filter(wordText=anagram).exists()
                if not wordExists:
                    word = Word(wordText=anagram)
                    word.save()
            return HttpResponseRedirect('/anagram/result/') # TODO: make this work
    else:
        form = forms.Form()
    return render(request, 'anagram/index.html', {'form' : form})

def result(request):
    # TODO: display word & anagrams here and in template
    return render(request, 'anagram/result.html')
