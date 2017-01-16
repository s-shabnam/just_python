fname = input("Enter file name: ")
if len(fname) < 1 : fname = "./src/mbox-short.txt"
try :
    file = open(fname)
except :
    print ('No such file')
    exit()

senderDict = dict()
lineList = list(file)
for line in lineList:
    if line == [] : continue
    if line.startswith("From "):
        lineWords = line.split()
        sender = lineWords[1]
        senderDict[sender] = senderDict.get(sender, 0) + 1

bigCount = None
bigSender = None
for sender, count in senderDict.items():
    if bigCount is None or count > bigCount :
        bigCount = count
        bigSender = sender
        
#print("Here is the most frecuent word : ", bigSender, ", and it is appered ", bigCount, " times. ")
print (bigSender, bigCount)