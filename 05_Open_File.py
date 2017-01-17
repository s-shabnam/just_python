#Read from file
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except: 
    print "No such file"
    exit()  
    
for line in fh:
    line = line.upper().strip()
    print line
