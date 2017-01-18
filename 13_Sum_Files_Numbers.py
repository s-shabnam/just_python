import re

fn = input("Enter file name: ")
if len(fn) < 1:
    fn = "./src/regex_sum_345021.txt"
try:
    file = open(fn)
except:
    print('No such file')
    exit()

total = 0
for line in file:
    lineNumberlist = re.findall('[0-9]+', line)
    if len(lineNumberlist) > 0:
        for element in lineNumberlist:
           total += int(element)
print(total)
