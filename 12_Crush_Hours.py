fname = input("Enter file name: ")
if len(fname) < 1 : fname = "./src/mbox-short.txt"
try :
    file = open(fname)
except :
    print ('No such file')
    exit()

hoursDict = dict()
lineList = list(file)
for line in lineList:
    if line == [] : continue
    if line.startswith('From ') :
        lineWords = line.split()
        time = lineWords[5]
        hour = time[:2]
        hoursDict[hour] = hoursDict.get(hour, 0) + 1

hourTuplesList = list()
for hour, count in hoursDict.items():
    hourTuplesList.append((hour, count))
   
hourTuplesList.sort()
 
for hour, count in hourTuplesList : 
     print (hour, count)
       
