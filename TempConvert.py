from __future__ import division

def Fah (temp):
        convert = (temp * 9)/5 + 32 
        return convert
        
        
def cel (temp):
        convert = (temp-32) * (5/9)
        return convert
        

InTemp = float(raw_input("Enter a Temperature in Fahrenheit and I will convert it to Celsius: "))

tempConv = cel(InTemp)

print "Your temperature in Celsius is",tempConv       

inTemp2 = float(raw_input("Enter a temperature in Celsius and I will convert it to Fahrenheit: "))

tempConv2 = Fah(inTemp2)

print "Your Temperature in Fahrenheit is",tempConv2




