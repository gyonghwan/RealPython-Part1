#Assignmment #2 
#Asks users to enter text and change specific characters and print modified string. 


#Rules

userInput = raw_input("Enter any string or phrase and I will convert it to leetspeak: ") 

rule1 = userInput.replace("a","4")
rule2 = rule1.replace("b","8")
rule3 = rule2.replace("e","3")
rule4 = rule3.replace("l","1")
rule5 = rule4.replace("o","0")
rule6 = rule5.replace("s","5")
rule7 = rule6.replace("t","7")

print "New phase is: ",rule7 



