"""
The main menu for the HVAC system. This menu allows the user to access the fan operations polling loop, graph functions or to change the system settings.
"""


from pymata4 import pymata4
import random
from HVAC_graph import graph
import polling_loop
from user_pin_functions import check_user_pin, setup_user_pin
from callback_functions import process_thermistor_data, check_thermistor_operation, check_fan_operation, object_detection_mode
from display import show_word



# Global variables
temp = 25 # NOTE: We need to figure out which function we are suppoesd to plug this value into.
graphing_time = 20
data = [22]
increasing = random.choice([True,False])
tempData = []
tempEverySecond = []
rateOfChange = []
#ultrasonic sensor
triggerPin = 8
echoPin = 9
buzzerLEDpin=7
first_reading = True # Flag to indicate first reading
#ambient temp. thermistor
ambTempData = []
ambTempEverySecond = []


def main_menu():
    """
    main_menu()
    This function is called to access the fan operations polling loop, graph functions or to change the system settings.

    """
    global tempEverySecond, ambTempEverySecond, rateOfChange
    
    polling_loop.board.set_pin_mode_sonar(triggerPin, echoPin, callback= object_detection_mode, timeout=200000)#sets the pins for the sensor
    polling_loop.board.set_pin_mode_digital_output(buzzerLEDpin)#sets digital input    
        
    try:
        show_word("Welcome")
        while True:
            # loop back to the main menu unless exited
            print("-----------------", '\033[1m' + "    Main Menu    " + '\033[0m', "-----------------", 
                '\033[0;32;40m' + "1: Fan Operation" + '\033[0m',
                '\033[0;35;40m' + "2: Graphing" + '\033[0m',
                '\033[0;34;40m' + "3: System Settings" + '\033[0m', 
                "4: Exit", "", sep="\n")
            
            # verify input
            operation = input("Enter value: ")
            while True:
                if operation == "1" or operation == "2" or operation == "3" or operation == "4":
                    break
                else:
                    operation = input("Enter a valid input (1, 2, 3 or 4): ")
            

            # operation 1: Fan operations
            if operation == "1":
                global data
                
                while True:
                    try:
                        cubicFeet = int(input(("What is the volume of the room in feet? ")))
                        flows = int(input(("How many times would you like the air to flow in and out of the room per hour? ")))
                        if cubicFeet > 0:
                            if flows > 0:
                                break
                        else:
                            print("Enter valid response ")
                    except KeyboardInterrupt:
                        quit()
                #start polling loop
                
                data = polling_loop.polling_loop(data, cubicFeet, flows)
                

            # operation 2: Graphing
            elif operation == "2":
                print("-----------------", '\033[1m' + " Graphing " + '\033[0m', "-----------------",
                     "1: Temperature vs Time",
                     "2: Rate of Change of Temperature vs Time",
                     "3: Ambient Temperature vs Time ",
                     "4: Return to Main Menu", "", sep="\n")
                # Check the users input
                option = input("Enter value: ")

                while True:
                    if option == "1" or option == "2" or option == "3" or option == "4":
                        break
                    else:
                        option = input("Enter a valid input (1, 2, 3 or 4): ")
                
                if option == '1':
                    graph(data[0][-graphing_time:], 'Temperature vs Time', 'TempGraph', graphing_time)                
                    main_menu()
                elif option == '2':
                    graph(data[2][-graphing_time:], 'Rate of Change of Temp. vs Time', 'ROCgraph', graphing_time)                
                    main_menu()
                elif option == '3':
                    graph(data[3][-graphing_time:], 'Ambient Temperature vs Time', 'AmbTempGraph', graphing_time)                
                    main_menu()
                elif option == '4':
                    main_menu()

            # operation 3: System settings
            elif operation == "3":
                show_sys_settings()
                
            # operation 4: Exit
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
        # polling_loop.board.digital_write(buzzerLEDpin, 0)
        # polling_loop.board.disable_digital_reporting(buzzerLEDpin)
        for i in range(13):
            polling_loop.board.digital_write(i, 0)
        polling_loop.board.shutdown()
        #polling_loop.board.reset()
        exit(0)
        
def show_sys_settings():
    import time
    #pin function
    check_user_pin()
    global temp, graphing_time
    startTime = time.time()

    # Print system message
    print("-----------------", '\033[1m' + " System Settings " + '\033[0m', "-----------------",
        "1: Change User Pin",
        "2: Change Temperature",
        "3: Graphing Time",
        "4: Exit", "", sep="\n")
    
    # Check the users input
    setting = input("Enter value: ")
    endTime = time.time()

    # If the user takes more than a minute between seeing the screen and making a selection, the program will exit
    if endTime - startTime > 60:
        print("You have been inactive for too long. Exiting back to main menu.\n")
        main_menu()
    while True:
        if setting == "1" or setting == "2" or setting == "3" or setting == "4":
            break
        else:
            setting = input("Enter a valid input (1, 2, 3 or 4): ")

    # If the operation is 1 then change the user pin
    if setting == "1":
        setup_user_pin()
        

    # If the operation is 2 then change the temperature    
    elif setting == "2":
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
    
    elif setting == "3":
        while True:
            x = input(f"Graphing displays values for the last: {graphing_time}s. Enter the new time in seconds: ")
            try: 
                graphing_time = int(x)
                if int(graphing_time) == float(graphing_time) and 0<=graphing_time<=120:
                    break
                else:
                    print("Please enter a positive integer value between 0 and 120.\n")
            except:
                print("Please enter a valid integer value between 0 and 120.\n")
        print(f"The graphing function will now display values from the last {graphing_time}s. \n")
    

if __name__ == "__main__":
    main_menu()
    

