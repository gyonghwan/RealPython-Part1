#Simulating Election of A B using Random function
#Condidate A has probability of winning 87% in Region 1, 65% in region 2 and 17% in Region 3. 
#If candidate A or B have average result for 2 or 3 region that condidate winds election 
#script will simulate election for 10,000 time and calculate average results. 
from __future__ import division
from random import random   

A1T = 0;
B1T = 0;
A2T = 0;
B2T = 0;
A3T = 0;
B3T = 0;
AT = 0;
BT = 0;
A2T = 0;
B2T = 0;
A3T = 0;
B3T = 0; 
R1 = 0;
R2 = 0;
R3 = 0;
AR = 0;
BR = 0;

SimTotal = 10000;

for R1 in range (1,SimTotal):
    PA1 = random()
    PB1 = random()
    if PA1 > PB1:
        AT += 1
    else:
        BT += 1
print "Total Simulated win for Candidate A in Region A is", AT
print "Total Simulated win for Candidate B in Region A is", BT
            
for R2 in range (1,SimTotal):
    PA2 = random()
    PB2 = random()
    if PA2 > PB2:
        A2T += 1
    else:
        B2T += 1

print "Total Simulated win for Candidate A in Region B is", A2T
print "Total Simulated win for Candidate B in Region B is", B2T
            
for R3 in range (1,SimTotal):
    PA3 = random()
    PB3 = random()
    if PA3 > PB3:
        A3T += 1
    else:
        B3T += 1
print "Total Simulated win for Candidate A in Region C is", A3T
print "Total Simulated win for Candidate B in Region C is", B3T
        
AVG_A1 = AT / SimTotal
AVG_B1 = BT / SimTotal
AVG_A2 = A2T / SimTotal
AVG_B2 = B2T / SimTotal
AVG_A3 = A3T / SimTotal
AVG_B3 = B3T / SimTotal

print "Average win for Candidate A in Region A is",AVG_A1
print "Average win for Candidate B in Region A is",AVG_B1
print "Average win for Candidate A in Region B is",AVG_A2
print "Average win for Candidate A in Region B is",AVG_B2
print "Average win for Candidate A in Region C is",AVG_A3
print "Average win for Candidate A in Region C is",AVG_B3   

if AVG_A1 > AVG_B1: 
    AR += 1
else:
    BR += 1

if AVG_A2 > AVG_B2:
    AR += 1
else: 
    BR += 1
    
if AVG_A3 > AVG_B3:
    AR += 1
else: 
    BR += 1 
    

if AR > BR:
    print "Candidate A has won the election"
else: 
    print "Candidate B has won the election"
    
    
            
            
