fname = input("Enter file name: ")
try :
    file = open(fname)
except :
    print ('No such file')
    exit()

resultList = list()
lineList = list(file)
for line in lineList:
    lineWords = line.split()
    for word in lineWords:
        if word not in resultList:
            resultList.append(word)

resultList.sort()
print (resultList)
