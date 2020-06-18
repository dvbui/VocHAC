from nltk.corpus import wordnet as wn

total_synset = {}


def load_synset():
    global total_synset
    f = open("wordlist_formatted.txt", "r")
    for line in f:
        word = line.strip()
        synsets = wn.synsets(word)
        for synset in synsets:
            total_synset[synset] = {}

