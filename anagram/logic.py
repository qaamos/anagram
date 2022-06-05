import itertools

def main():
    word = ""
    wordPermutations = []
    anagrams = {}
    # in final version dictionary will be an actual dictionary found in database
    dictionary = ["kissa"]

    word = input("Enter a word: ")
    wordPermutations = generatePermutations(word)
    anagrams = findRealWords(wordPermutations, dictionary)
    print(anagrams)
    return 1

def generatePermutations(word):
    permutations = []
    permutations = list(itertools.permutations(word))
    permutations = [''.join(permutation) for permutation in permutations]
    return permutations

def findRealWords(permutations, dictionary):
    realWords = {}
    realWords = set(permutations).intersection(dictionary)
    return realWords

main()
