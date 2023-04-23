
import time
from pymata4 import pymata4
import random
import matplotlib.pyplot as plt
from HVAC_graph import graph, randomised_data
from callback_functions import process_thermistor_data, check_thermistor_operation, check_fan_operation
import polling_loop
from Pin import pin
#import polling function
#import pin function

# Global variables
temp = 25 # NOTE: We need to figure out which function we are suppoesd to plug this value into.
data = [22]
increasing = random.choice([True,False])

"""
main_menu()
This function is called to access the fan operations polling loop, graph functions or to change the system settings.

"""

def main_menu():
    try:
        while True:
            #loop back to the main menu unless exited
            print("-----------------", '\033[1m' + "    Main Menu    " + '\033[0m', "-----------------", 
                "1: Fan Operation",
                "2: Graphing",
                "3: System Settings", 
                "4: Exit", "", sep="\n")
            
            #verify input
            operation = input("Enter value: ")
            while True:
                if operation == "1" or operation == "2" or operation == "3" or operation == "4":
                    break
                else:
                    operation = input("Enter a valid input (1, 2, 3 or 4): ")
            

            #operation 1: Fan operations
            if operation == "1":
                global data
                #start polling loop
                data = polling_loop.polling_loop(data)
                

            #operation 2: Graphing
            elif operation == "2":
                graph(data)
                continue

            #operation 3: System settings
            elif operation == "3":
                #pin function
                pin()
                global temp
                while True:
                    x = input(f"The current temperature is set to {temp} degrees celcius. Enter the new temperature value: ")
                    try: 
                        temp = int(x)
                        if int(temp) == float(temp) and 15<=temp<=30:
                            break
                        else:
                            print("Please enter a positive integer value between 15 and 30.\n")
                    except:
                        print("Please enter a valid integer value between 15 and 30.\n")
                print(f"The new temperature is {temp} degrees celcius. \n")
                

            elif operation == "4":
                print("\nExiting...\n")
                print(5*"\n")
                print("You have exited the program")
                print("\n")
                break
    except KeyboardInterrupt:
        print("\nExiting...\n")
        print(5*"\n")
        print("You have exited the program")
        print("\n")
        exit(0)
        

if __name__ == "__main__":
    main_menu()
    

