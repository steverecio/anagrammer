import random

lexicon = {}

def addWordToLexicon(word):
    lex = lexicon

    for i,char in enumerate(word):
        end = False
        if i == len(word)-1:
            end = True
        if char in lex:
            if end:
                lex[char][0] = end
        else:
            lex[char] = [end, {}] # tuples are immutable :(
        lex = lex[char][1]

def isWord(word):
    lex = lexicon
    for i,char in enumerate(word):
        end = False
        if i == len(word)-1:
            end = True

        if char not in lex:
            return False
        elif end and lex[char][0]:
            return True
        else:
            lex = lex[char][1]

    return False

def init():
    with open('wordlist.txt') as f:
        for line in f:
            word = line.strip().lower()
            if word.isalpha():
                addWordToLexicon(word)

def findAnagrams(word, numTries=100):
    anagrams = []
    for i in range(numTries):
        shuffled = ''.join(random.sample(word, len(word)))
        if isWord(shuffled):
            anagrams.append(shuffled)
    return set(anagrams)

if __name__ == '__main__':
    init()
    anagrams = findAnagrams('steven', 1000)
    for anagram in anagrams:
        print anagram
