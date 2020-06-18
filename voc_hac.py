from nltk.corpus import wordnet as wn

total_synset = {}
index_to_synset = []


def load_synset():
    global total_synset, index_to_synset
    f = open("wordlist_formatted.txt", "r")
    for line in f:
        word = line.strip()
        synsets = wn.synsets(word)
        for synset in synsets:
            total_synset[synset] = {}

    for synset in total_synset:
        total_synset[synset] = len(index_to_synset)
        index_to_synset.append(synset)

