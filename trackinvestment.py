def invest (A,R,T):
        V = A * (1 + R) ** T
        return V
        
amount = raw_input("Principal Amount: ") #User input of principal amount in string 
rate = raw_input("Annual rate of return: ") #User input of interest rate in string
time = raw_input("Enter number of year of investment: ")
        
A = float(amount) #Converting principal amount in string to floating value 
R = float(rate) #converting interest rate in string to flaoting value 
T = int(time) #converting number of year in integer 
        
for counter in range (1,T+1):
        result = invest(A,R,counter)
        print "Year {}: {}".format(counter,result)
                
        
        
        
        
