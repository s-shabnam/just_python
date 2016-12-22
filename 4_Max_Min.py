#Prints min and max of values entered by user

largest = None
smallest = None

largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
        if smallest is None : smallest = num
        elif num < smallest : smallest = num
        if largest is None : largest = num 
        elif num > largest : largest = num
    except:
        print "Invalid input"
        continue
    
print "Maximum is", largest
print "Minimum is", smallest
