# Get two numbers from user and calculate exponent of two numbers. 




baseNumber = raw_input("Enter a base: ")
exponentNumber = raw_input("Enter an exponent: ")

result = float(baseNumber) ** float(exponentNumber) 

print "{} to the power of {} = {}".format(baseNumber,exponentNumber,result) 

