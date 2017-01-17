fname = input("Enter file name: ")
if len(fname) < 1 : fname = "./src/mbox-short.txt"
try :
    file = open(fname)
except :
    print ('No such file')
    exit()

wordDict = dict()
lineList = list(file)
for line in lineList:
    if line == [] : continue
    lineWords = line.split()
    for word in  lineWords :
        wordDict[word] = wordDict.get(word, 0) + 1

bigCount = None
bigWord = None
for word, count in wordDict.items():
    if bigCount is None or count > bigCount :
        bigCount = count
        bigWord = word
        
print("Here is the most frecuent word : ", bigWord, ", and it is appered ", bigCount, " times. ")
