def doubles (num):
        result = int(num) * 2
        return result
        
        

input = raw_input("Enter the number for to get doubled :")

for counter in range (1,4):
        print "The double of the ",input,"is :",doubles(input)
        input = doubles(input)
        

