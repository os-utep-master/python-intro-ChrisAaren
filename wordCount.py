import os
import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

if not os.path.exists(inputFile):
    print("This file does not exist")
    exit()

def wordCounter():
    f = open(inputFile, "r")
    contents = f.read()
    words = contents.split()
    words = [i.strip('\n') for i in words]
    words = [i.replace('"', '') for i in words]
    unwanted = ',.--:;'''
    words = [i.lower() for i in words]
    dictionary = {}
    for i in words:
        word = i.strip(unwanted)
        if word not in dictionary:
            dictionary[word] = 0
        dictionary[word] += 1
    writeToFile(dictionary)


def writeToFile(Dict):
    f = open(outputFile, "w+")
    for key in sorted(Dict.keys()):
        f.write("%s %s \r\n" % (key, Dict[key]))


if __name__ == "__main__":
    wordCounter()
