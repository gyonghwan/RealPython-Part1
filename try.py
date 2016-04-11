status = False

while status != True:
    try:
        answer = int(raw_input("Enter an integer: "))
        status = isinstance(answer,int)
    except ValueError:
        print answer,"is not an integer" 
         
print answer,"is an integer" 

