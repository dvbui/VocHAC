from nltk.corpus import wordnet as wn

total_synset = {}
index_to_synset = []
distance_matrix = []


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


def compute_distance_matrix():
    global distance_matrix
    distance_matrix = [[0] * len(total_synset)] * len(total_synset)
    for i in range(len(index_to_synset)):
        for j in range(i+1, len(index_to_synset)):
            similarity = index_to_synset[i].wup_similarity(index_to_synset[j])
            if similarity is None:
                similarity = 0
            distance_matrix[i][j] = 1 - similarity


load_synset()
compute_distance_matrix()
