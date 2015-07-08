def Fahernheit(Temp):
	Cel = (Temp - 32) * (5/9)
	return Cel

	
def Celsius(Temp):
	Fahern = Temp * (9/5) + 32
	return Fahern

	
input_temp = raw_input("Enter temperate you want to convert to: ")

convert_temp = int(input_temp)

convert_Fahern = Fahernheit(convert_temp)
print "Your temperate in Celsius is: ",convert_Fahern
convert_cel = Celsius(convert_temp)
print "your temperate in Fahernheit is: ", convert_cel

