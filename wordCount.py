import os
import sys
import re

inputFile = sys.argv[1]
outputFile = sys.argv[2]

if not os.path.exists(inputFile):
    print("This file does not exist")
    exit()


def wordCounter():
    try:
        f = open(inputFile, "r")
        contents = f.read()
        unwanted_characters = "[\"\'!?;:,.-]"
        contents = re.sub(unwanted_characters, " ", contents)
        words = contents.split()
        words = [i.lower() for i in words]
        dictionary = {}
        for i in words:
            if i not in dictionary:
                dictionary[i] = 0
            dictionary[i] += 1
        writeToFile(dictionary)
    finally:
        f.close()

def writeToFile(Dict):
    try:
        f = open(outputFile, "w+")
        for key in sorted(Dict.keys()):
            f.write("%s %s \r\n" % (key, Dict[key]))
    finally:
        f.close()

if __name__ == "__main__":
    wordCounter()
