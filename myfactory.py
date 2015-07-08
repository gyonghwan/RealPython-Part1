# writing script to identify factor number for the integer user input

def factor ():
    userinput = raw_input("please enter positive integer: ")
    last_prime = int(userinput)
    index = 1

    while last_prime >= index:
        if (int(userinput) % index) == 0:
            print "{} is a divisor of {}".format(index,last_prime)
            index = index + 1
        else:
            index = index + 1

factor()
