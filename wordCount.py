import re


def wordCounter():
    f = open("declaration.txt", "r")
    contents = f.read()
    words = contents.split()
    words = [i.replace('"', '') for i in words]
    unwanted = ',.\n--" ":'
    words = [i.lower() for i in words]
    dictionary = {}
    for i in words:
        word = i.strip(unwanted)
        if word not in dictionary:
            dictionary[word] = 0
        dictionary[word] += 1
    writeToFile(dictionary)


def writeToFile(Dict):
    f = open("output.txt", "w+")
    for key in sorted(Dict.keys()):
        f.write("%s %s \r\n" % (key, Dict[key]))


if __name__ == "__main__":
    wordCounter()
