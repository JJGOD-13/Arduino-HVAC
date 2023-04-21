# By Jayant Godse
# Date: 18/04/2023
"""
This program will outline how the arduino will continuosly read data from the sensors and then use that data to control other functions.

"""
# Import the required libraries
import time
from pymata4 import pymata4
import random
from Menu import main_menu
from HVAC_graph import graph, randomised_data
from callback_functions import process_thermistor_data

# Initialise the Arduino
board = pymata4.Pymata4()


# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3


# Initialise pins
PIN_1 = 0
PIN_2 = 1

# Polling Loop Cycle Length
# INPUT: Start and end values
# OUTPUT: The amount of time in seconds that the polling cycle ran for
def polling_loop_cycle_length(start, end):
    # Check if the start and end values are integers
    try:
        start = int(str(start))  
    except ValueError:
        print("Value isn't an integer")
        exit(1) 
    try:
        end = int(str(end))  
    except ValueError:
        print("Value isn't an int")
        exit(1)
    # Check if the end value is greater than the start value
    if not end > start:
        print("End must be greater than start")
        exit(1)

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
    
# Generate Random Sequence
# INPUT: NOne
# OUTPUT: A random sequence of values


# Polling Loop

if __name__ == "__main__":

    while True:
        try:
            # Start the timer
            startTime = time.time()

            # Read the data from the sensors
            temp = board.analog_read(PIN_1)

            # Generate a random sequence
            randomSequence = generate_random_sequence()

            # End the timer
            endTime = time.time()

            # Calculate the cycle length
            cycleLength = polling_loop_cycle_length(startTime, endTime)
            print(f"Cycle Length: {cycleLength} seconds")
        
        except KeyboardInterrupt:


            main_menu()
