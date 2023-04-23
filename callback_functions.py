# Author: Jayant Godse
# Usage: This file will contain the callback functions that will be used in the polling loop

# Import the required libraries
import time
from pymata4 import pymata4
import random
import math


# Thermistor Callback Function

def process_thermistor_data(data): 
    """
    This function will parse the data from the thermistor and return a list of  average temperature values every second which can then be graphed

    INPUT: data: [pin_mode, pin, current_reported_value,  timestamp] {This is from the arduino}
    
    OUTPUT: A list of average temperature values every second {tempEverySecond}
    
    DEPENDENCIES: math, require 2 variables called tempData = [] and tempEverySecond = [] to be defined globally

    NOTE: This function still does some finicky stuff. It doesn't seem to properly break whenever a keyboard interrupt is called. 
          I feel like this is because the function is called far to often. I'm not sure how to fix this.
    """
    #GLOBAL VARIABLES
    global tempData
    global tempEverySecond

    tempData.append([data[2],data[3]]) # data is the Raw data from Thermistor
    timeTaken = data[3] - tempData[0][1]
    print(f'value = {tempData[-1][0]}, time = {round(timeTaken, 2)} ')

    if int(timeTaken) >= 1:
        avgTemp = sum(tempData[0]) / len(tempData)
        avgTemp = round(((-21.21)*math.log(avgTemp/1000))+72.203, 2) # NOTE: Need to calibrrate this. Change the constants.
        tempEverySecond.append(avgTemp)
        tempData.clear()

def check_thermistor_operation(thermistorPin):
    """
    This function will check if the thermistor is working properly

    """
    #TODO

def check_fan_operation(fanPin):
    """
    This function will check if the fan is working properly

    """
    #TODO