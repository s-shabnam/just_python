
# Calculate gross pay as : Pay the hourly rate for the hours up to 35 and 2 times the hourly rate for all hours worked above 35 hours.
#Program Constants
baseHours =35.0
extraPayCoefficient = 2

#function definition
def computepay(hours,payRate):

    if hours <= baseHours :
        totalPay = hours*payRate
    else :
        totalPay = baseHours*payRate + extraPayCoefficient*(hours - baseHours)*payRate

    return totalPay

#Input data
try :
	hours = float(raw_input("Enter worked hours please:"))
	payRate = float(raw_input("Enter pay rate to use please:"))
except:
	print "Please enter valid data"
	quit()

totalPay = computepay(hours,payRate)
print totalPay
