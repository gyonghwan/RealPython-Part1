from capitals import capitals_dict
import random

randomState = random.choice(capitals_dict.keys())
randomCapital = capitals_dict[randomState]
print "The State is ",randomState
answer = raw_input("Enter the Capital: ")

while answer.upper() != randomCapital.upper():
    randomState = random.choice(capitals_dict.keys())
    randomCapital = capitals_dict[randomState]
    print "You entered wrong capital! Please Enter Capital for ",randomState
    answer = raw_input("Enter the capital: ")

    
    




