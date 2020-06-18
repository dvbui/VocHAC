f = open("wordlist.txt", "r")
total = {}
for line in f:
    words = line.strip().split(' ')
    for word in words:
        total[word] = {}
f.close()

g = open("wordlist_formatted.txt", "w")
for word in total:
    g.write(word+'\n')
g.close()

