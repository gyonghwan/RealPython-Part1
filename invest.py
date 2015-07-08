# Investment Calculator by taking Original Loan amount, interest Rate and loan rates then calculate maturity amount.

#function investment
def invest (amount, rate, time):
      print "principal Amount: ",amount
      print "Annual Rate of Return: ",rate

      for t in range(1, time + 1):
            amount = amount + (amount*rate)
            print "year {} has: $".format(t), amount
      print

print invest(100, 0.05, 2)
