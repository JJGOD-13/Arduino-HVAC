# By Jayant Godse
# Date: 18/04/2023
"""
This program will outline how the arduino will continuosly read data from the sensors and then use that data to control other functions.

"""
# Import the required libraries
import time
from pymata4 import pymata4
from Menu import main_menu
import HVAC_graph
from callback_functions import process_thermistor_data, check_thermistor_operation, check_fan_operation

# Initialise the Arduino
# board = pymata4.Pymata4()


# Callback data indices
callbackPinMode = 0
callbackPin = 1
callbackValue= 2
callbackTime = 3


# Initialise pins
thermistorPin = 0
fanPin = 1
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
    OUTPUL: returnData: [randomSequence, cycleLength]
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
            check_fan_operation(fanPin)

            # Setup the pins
            
            # board.set_pin_mode_analog_input(thermistorPin, process_thermistor_data)
            

            # Generate a random sequence
            
            randomSequence = HVAC_graph.randomised_data(data)

            # End the timer
            
            endTime = time.time()

            # Calculate the cycle length
            
            cycleLength = polling_loop_cycle_length(startTime, endTime)
            print(f"Cycle Length: {cycleLength} seconds")

            # Return the data to the main menu

            returnData = randomSequence
            
            

        except KeyboardInterrupt:
            return returnData
            

# Polling Loop

if __name__ == "__main__":

    polling_loop()
