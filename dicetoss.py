from __future__ import division
from random import  randint

one = 0;
two = 0;
three = 0;
four = 0;
five = 0;
six = 0;

for T in range(0,10000):
        toss = randint(1,6)
        if toss == 1:
            one += 1
        elif toss == 2:
            two += 1
        elif toss ==3:
            three += 1
        elif toss == 4:
            four += 1
        elif toss == 5:
            five += 1
        else:
            six += 1

print one,two,three,four,five,six

oneave = one / 10000
twoave = two / 10000
thrave = three / 10000
fouave = four / 10000
fivave = five / 10000
dixave = six / 10000

print oneave, twoave, thrave, fouave, fivave, dixave 


