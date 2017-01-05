
#The program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 


fname = raw_input("Enter file name: ")
try :
    fh = open(fname)
except :
    print 'No such file'
    exit()

count = 0
total = 0.00
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    index = line.find(":")
    subString = line[index+1:].strip()
    newN = float(subString)
    total = total + newN
print "Average spam confidence:",total/count
