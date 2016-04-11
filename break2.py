input = int(raw_input("Enter a number to be listed: "))

for i in range(0,input+1):
    if (i % 3) == 0:
        continue
    else:
        print i,"is not multiple of 3" 
        
    
