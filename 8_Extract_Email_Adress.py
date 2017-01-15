fname = input("Enter file name: ")
if len(fname) < 1 : fname = "./src/mbox-short.txt"
try :
    file = open(fname)
except :
    print ('No such file')
    exit()

emailList = list()
count = 0
lineList = list(file)
for line in lineList:
    if line.startswith('From '):
        lineWords = line.split()
        email = lineWords[1]
        if email not in emailList:
            emailList.append(email)
            print (email)
            count += 1

emailList.sort()
# print (emailList)
print ("There were", count, "lines in the file with From as the first word")
