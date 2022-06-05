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

def connectToDb():
    path = os.getcwd()
    parent = os.path.dirname(path)
    connection = sqlite3.connect(parent+"/db.sqlite3")
    return connection

def generatePermutations(word):
    permutations = []
    permutations = list(itertools.permutations(word))
    permutations = [''.join(permutation) for permutation in permutations]
    return permutations

def findWordsFromDict(permutations, connection):
    realWords = []
    cursor = connection.cursor()
    for permutation in permutations:
        # SQL query should probably be sanitized
        for result in cursor.execute("SELECT word FROM dictionary WHERE word LIKE '" + permutation + "'"):
            realWords.append(result[0])
    return realWords

main()
