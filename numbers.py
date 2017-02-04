largest = None
smallest = None
inp_num = 0
while True:
    
   # Check for Valid Num
    usr_input = raw_input("Enter a number: ")
    if usr_input == "done" : break
    try:
        inp_num = int(usr_input)
    except ValueError: 
        print "Invalid input"
   # End checking - must be an integer or done
    if inp_num < largest:
        smallest = inp_num
    elif inp_num > largest:
		largest = inp_num
   # End assignment 	
print "Maximum is", largest
print "Minimum is", smallest