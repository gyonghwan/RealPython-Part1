#Better way to utilize the function to write invest script.

def invest(amount, rate):
        roi = amount + (amount*rate)
        return (roi)

investment_amount = raw_input("Enter amount that you want to invest: $")
investment_rate = raw_input("Enter invested rate in decemal (ex. 0.03 for 3%): ")
investment_length = raw_input("Enter length of investment in year: ")

for i in range (1, int(investment_length) + 1):
    newAmount = invest(int(investment_amount),float(investment_rate))
    print "Year {} : ".format(i),newAmount
    
