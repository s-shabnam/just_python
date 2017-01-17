fname = input("Enter file name: ")
if len(fname) < 1 : fname = "./src/mbox-short.txt"
try :
    file = open(fname)
except :
    print ('No such file')
    exit()

wordsDict = dict()
lineList = list(file)
for line in lineList:
    if line == [] : continue
    else :
        lineWords = line.split()
        for word in lineWords:
            wordsDict[word] = wordsDict.get(word, 0) + 1

print(sorted([(count, word) for word, count in wordsDict.items()], reverse  = True))

       
