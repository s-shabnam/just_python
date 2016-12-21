# Calculate gross pay as : Pay the hourly rate for the hours up to 35 and 2 times the hourly rate for all hours worked above 35 hours.

# Program constants
baseHours =35.0
extraPayCoefficient = 2.0

#Input data
hours = float(raw_input("Enter Hours please:"))
payRate = float(raw_input("Enter Pay Rate please:"))

extraHours = hours - baseHours
basePay = baseHours*payRate

if extraHours <= 0 :
	totalPay = basePay
else :
    totalPay = basePay + extraPayCoefficient*extraHours*payRate
    
print totalPay
