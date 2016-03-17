#Factor.py 
#When user enters an integer, the script will list all factor numbers. 

Number = raw_input("Enter a Number and I will list all factors: ")

N = int(Number) #convert string input to integer format. 

I = 1

while I <= N: 
    if (N % I) == 0:
        print "{} is a divisor of {}".format(I,N)
        I = I + 1
    else:
        I = I + 1


