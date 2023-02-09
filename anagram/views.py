import re
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django import forms

from anagram.models import Word
from anagram.models import Anagram
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
            wordExists = Word.objects.filter(wordText=input.capitalize()).exists()
            if not wordExists and anagrams != []:
                newWord = Word(wordText=input.capitalize())
                newWord.save()
                for anagram in anagrams:
                    newAnagram = Anagram(word=newWord, anagramText=anagram)
                    newAnagram.save()
            return HttpResponseRedirect('/anagram/result/') # TODO: make this work
            
    else:
        form = forms.Form()
    return render(request, 'anagram/index.html', {'form' : form})

def result(request):
    # TODO: display word & anagrams here and in template
    return render(request, 'anagram/result.html')
