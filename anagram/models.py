from django.db import models

# Create your models here.
class Word(models.Model):
    wordText = models.CharField(max_length=200)
    def __str__(self):
        return self.wordText

class Anagram(models.Model):
    word = models.ForeignKey(Word, on_delete = models.CASCADE)
    anagramText = models.CharField(max_length=200)
    def __str__(self):
        return self.anagramText
