# Find grade by using score (0.0 to 1.0). The following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

try:
	score = float(raw_input("Enter Score: "))
except :
    print "Enter valid score please."
    quit()
    
#looking for grade
if (score <= 1.0) & (score >= 0.0) :   
    if score >= 0.9:
        print "A"
    elif score >= 0.8:
        print "B"
    elif score >= 0.7:
        print "C"
    elif score >= 0.6:
        print "D"
    elif score < 0.6:
        print "F"
else :
    print "Enter a score between 0.0 and 1.0."

    
