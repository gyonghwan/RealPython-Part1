# Review exercise to understand if else statement
# user input string and calucate string length


def checklength ():
    user_input = raw_input("Please enter any string and we will calculate length: ")
    if len(user_input) < 5:
        print "your string is less than 5 characters"
    elif len(user_input) > 5:
        print "your string is grater than 5 characters"
    else:
        print "your string is 5 characters"


checklength ()
