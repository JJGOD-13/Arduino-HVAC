# Author: Jayant Godse
# Usage: This file will contain the callback functions that will be used in the polling loop

# Import the required libraries
import time
from pymata4 import pymata4
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
    from polling_loop import tempEverySecond, tempData, rateOfChange

    rateOfChangeFactor = 5
    
    tempData.append([data[2]*(5/1023),data[3]]) # data is the Raw data from Thermistor
    timeTaken = data[3] - tempData[0][1]
    # print(f'value = {tempData[-1][0]}, time = {round(timeTaken, 2)} ')

    if int(timeTaken) >= 1:
        #calculating average voltage reading in V   
        sum = 0
        for data in tempData:
            sum+=data[0]
        avgVol = (sum / len(tempData))
        #calculating resistance of thermistor via voltage divider in Kilo ohms
        resistance = ((5100*avgVol)/(5-avgVol))/1000
        #converting resistance to degrees celsius
        avgTemp = round((-21.21*math.log(resistance))+72.203, 2) 
        tempEverySecond.append(avgTemp)
        tempData.clear()
        if len(tempEverySecond) >= rateOfChangeFactor:
            roc = (tempEverySecond[-1]-tempEverySecond[-5])/rateOfChangeFactor
            rateOfChange.append(round(roc,3))

def check_thermistor_operation(thermistorPin):
    """
    This function will check if the thermistor is working properly

    """
    from Menu import main_menu
    from polling_loop import board
    # Check if pin works otherwise send potential solution and shutdown board properly
    try:
        board.set_pin_mode_analog_input(thermistorPin, process_thermistor_data)
        print("Thermistor is working properly")
        
    except:
        print('\033[1;32;40m' + "Thermistor is not working properly" + '\033[0m')
        print("Try checking the pin and connections")
        board.shutdown()
        main_menu()


def check_fan_operation(fanPin1, fanPin2):
    """
    This function will check if the fan is working properly

    """
    from Menu import main_menu
    from polling_loop import board
    # Check if pin works otherwise send potential solution and shutdown board properly
    try:
        board.set_pin_mode_digital_output(fanPin1)
        board.set_pin_mode_digital_output(fanPin2)
        print("Fan is working properly")
        
    except:
        print('\033[1;32;40m' + "Fan is not working properly" + '\033[0m')
        print("Try checking the pin and connections")
        board.shutdown()
        main_menu()
