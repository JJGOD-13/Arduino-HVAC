# By Jayant Godse
# Date: 18/04/2023
"""
This program will outline how the arduino will continuosly read data from the sensors and then use that data to control other functions.

"""
# Import the required libraries
import time
from pymata4 import pymata4
from Menu import temp
from callback_functions import process_thermistor_data, check_thermistor_operation, check_fan_operation
from motor import control_motor

# Initialise the Arduino
board = pymata4.Pymata4()

# Global Variables
tempData = []
tempEverySecond = []
global temp

# Callback data indices
callbackPinMode = 0
callbackPin = 1
callbackValue= 2
callbackTime = 3


# Initialise pins
thermistorPin = 0
fanPin1 = 5
fanPin2 = 6
ledPin = 2
displayPins = [] #TODO Will be a list of pins that will be used for the 7 segment display

#TODO Add more pins as we figure out where to place things


def polling_loop_cycle_length(start, end):
    """
    Polling Loop Cycle Length
    INPUT: Start and end values
    OUTPUT: The amount of time in seconds that the polling cycle ran for
    """

    # Check if the start and end values are integers
   

    # Def the cycle length    

    cycleLength = end - start

    # Check that the cycle length is greater than 1 and less than 5

    if cycleLength < 1: # if cycle length is less than 1 second, set it to 1
        cycleLength = 1
        return cycleLength
    elif cycleLength > 5: # if the cycle length is greater than 5 seconds, cap it at 5
        cycleLength = 5
        return cycleLength
    else:
        return round(cycleLength, 2)
    
def polling_loop(data):
    """
    This function will run the polling loop
    OUTPUT: returnData: [tempEverySecond, cycleLength]
    """
    returnData = []
    while True:
        try:
            # Make the loop sleep every second to get the time correct 
            
            time.sleep(1)

            # Start the timer
            
            startTime = time.time()

            # Check if all componenets are working
            
            check_thermistor_operation(thermistorPin)
            check_fan_operation(fanPin1, fanPin2)

            # Setup the pins
            
            board.set_pin_mode_analog_input(thermistorPin, process_thermistor_data)
#             print(f'The current temperature is: {tempEverySecond[-1]}°C')
           
            # turning motor on and off
            #goal range = (23,27) --> goal temp is 25
            if tempEverySecond < temp-2: #too cold
                direction = 'clockwise'
                if (temp-2) - tempEverySecond  <1:
                    speed = 100
                    print('Fan set to low speed and moving heat into room') 
                elif (temp-2) - tempEverySecond <3:
                    speed = 150
                    print('Fan set to medium speed and moving heat into room') 
                elif (temp-2) - tempEverySecond >5:
                    speed = 200
                    print('Fan set to high speed and moving heat into room') 
            elif tempEverySecond > temp+2: #too hot
                direction = 'anticlockwise'
                if tempEverySecond - (temp+2) <1:
                    speed = 100
                    print('Fan set to low speed and moving heat out of room') 
                elif tempEverySecond - (temp+2) <3:
                    speed = 150
                    print('Fan set to medium speed and moving heat out of room') 
                elif tempEverySecond - (temp+2) >5:
                    speed = 200
                    print('Fan set to high speed and moving heat out of room') 
                else:           
                    speed = 0
                
            control_motor(direction,speed)
        

            # End the timer
            
            endTime = time.time()

            # Calculate the cycle length
            
            cycleLength = polling_loop_cycle_length(startTime, endTime)
            print(f"Cycle Length: {cycleLength} seconds")
            print(f"Temperature: {tempEverySecond[-1]}°C")

            # Return the data to the main menu

            returnData = {tempEverySecond, cycleLength}
            
            

        except KeyboardInterrupt:
            return returnData
            

# Polling Loop

if __name__ == "__main__":

    polling_loop()
