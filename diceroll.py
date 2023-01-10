import random
import time
while True:
    print(""" 1. Roll the dice                 2.Exit         """)
    user = int(input("Select an option\n"))
    if user == 1:
        number = random.randint(1,6)
        print("rolling ...")
        time.sleep(5) 
        print("Done")
        time.sleep(2)
        print(number)
        break
    else:
        break
