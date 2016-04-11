from __future__ import division
from random import  randint


stop = "Y"

while stop != "N":
    toss = randint(1,6)
    print "This dice toss came out as",toss
    stop = raw_input("Would you like to continue?(Enter N to quit)") 
    
print "toss ended" 


