birthday = {'Luke Skywalker':'5/24/19','Obi-Wan Kenobi':'3/11/57','Darth Vader':'4/1/41'}

check_bday = raw_input("enter the name for birthday check: ")

if not check_bday in birthday:
    print "unknown"
else:
    print check_bday,birthday[check_bday]




    

