#sys module provides functions and variables used to manipulate diffrent parts of the 
# python runtime environmrnt
import sys
#sys.exit() ##will stop python execution

#sys.argv of sys modules
#sys.argv returns a list of commandline argument passed to a python script

if len(sys.argv) != 3:
    print("usage")
    print(f"{sys.argv[0]} <your require string> <lower|upper|title>")
    sys.exit()
usr_str=sys.argv[1]
usr_action=sys.argv[2]

if usr_action == "lower":
    print(usr_str.lower())
elif usr_action == "upper":
    print(usr_str.upper())
elif usr_action == "title":
    print(usr_str.title())
else:
    print("Your option is invalid")    


