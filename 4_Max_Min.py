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
        if num < smallest : smallest = num
        if largest is None : largest = num 
        if num > largest : largest = num
    except:
        print "Enter valid input , integer number or done to exit"
 
print "Maximum is", largest
print "Minimum is", smalles
