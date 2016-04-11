from __future__ import division
from random import randint

heads = 0;
tails = 0;

for T in range(0,100):
    while randint(0,1) == 0:
        tails += 1
        print tails,heads
    heads += 1
    
print "heads / tails", heads/tails  

