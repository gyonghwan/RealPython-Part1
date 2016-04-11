from random import randint 

trials = 10000;
flips = 0;
subflips =0;
toss = 0;
nextToss = 0;
nexttossTotal = 0;
T = 0;

for T in range(0,trials):
    toss = randint(0,1)
    #print "First Toss is",toss
    nextToss = randint(0,1)
    #print "2nd Toss is",nextToss  
    if nextToss != toss:
        flips += 1
        #print "Toss Total",flips
    else:
        while (nextToss == toss):
            nextToss = randint(0,1)
            subflips += 1
            #print "Keep tossing", nextToss
            if nextToss != toss:
                flips += 1
                #print "Next Toss is has different result and adding to total",flips 
                break
            
totalflip = flips + subflips
AverageFlips = totalflip / trials

print "total number of flips are",totalflip
print "Average Flips are",AverageFlips





    
