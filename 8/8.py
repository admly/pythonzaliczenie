import sys
from collections import Counter

pathToFiles = "./"
filesToParse = sys.argv
filesToParse.pop(0)
most_popular = 10

for file in filesToParse:
    with open(pathToFiles + file, 'r+') as f:
        string = ""
        wordcount = Counter(f.read().split())
        for entry in wordcount.most_common(most_popular):
            string += "word: '" + entry[0] + "' count: " + str(entry[1]) + "; "
        f.write(f.read() + '\n' + string)
        f.close()
