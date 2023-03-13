import re
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
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
            oldWordList = Word.objects.filter(wordText=input.capitalize())

            # if word and anagrams have already been generated
            if oldWordList:
                oldWord = oldWordList[0]
                return HttpResponseRedirect(reverse('anagram:list', args=(oldWord.id,)))
            # if user inputs a new word
            anagrams = logic.webRequest(input)
            if anagrams != []:
                newWord = Word(wordText=input.capitalize())
                newWord.save()
                for anagram in anagrams:
                    newAnagram = Anagram(word=newWord, anagramText=anagram)
                    newAnagram.save()
                return HttpResponseRedirect(reverse('anagram:list', args=(newWord.id,)))
            
    else:
        form = forms.Form()
    return render(request, 'anagram/index.html', {'form' : form}) # TODO: make this prettier

def list(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    anagrams = get_list_or_404(Anagram, word=word_id)
    return render(request, 'anagram/list.html', {'word': word, 'anagrams': anagrams})
