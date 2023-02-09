import itertools
import sqlite3
import os


def main():
    word = ""
    wordPermutations = []
    anagrams = []

    con = connectToDb()
    word = input("Enter a word: ")
    wordPermutations = generatePermutations(word)
    anagrams = findWordsFromDict(wordPermutations, con)
    print(anagrams)
    con.close()
    return 1


def webRequest(word):
    wordPermutations = []
    anagrams = []

    con = connectToDb()
    wordPermutations = generatePermutations(word)
    anagrams = findWordsFromDict(wordPermutations, con)
    con.close()
    return anagrams

def connectToDb():
    path = os.getcwd()
    parent = os.path.dirname(path)
    connection = sqlite3.connect(parent+"/anagram/db.sqlite3")
    return connection

# TODO: optimize this so it doesn't crash on long words
def generatePermutations(word):
    permutations = []
    permutations = list(itertools.permutations(word))
    permutations = [''.join(permutation) for permutation in permutations]
    return permutations

def findWordsFromDict(permutations, connection):
    realWords = []
    cursor = connection.cursor()
    for permutation in permutations:
        # TODO: SQL query should probably be sanitized better
        results = cursor.execute("SELECT word FROM dictionary WHERE word LIKE '%s'"%(permutation))
        for result in results:
            # check if word is already in realWords 
            try:
                realWords.index(result[0])
            # if not, add it
            except:
                realWords.append(result[0])
    return realWords

