import time
from pymata4 import pymata4
# Author: Jayant Godse
# Usage: This file will contain the callback functions that will be used in the polling loop

#ultrasonic sensor
def object_detection_mode(data):
    """ 
    uses ultrasonic sensor to detect objects. if it senses an object greater than 5cm away, 
    it will flash a blue light with a frequency of 1hertz and beep continously.
    INPUTS: power from arduino
    OUTPUTS:flashing LED and beeping noise(if condition is met) 
    """
    from polling_loop import board
    from Menu import triggerPin, first_reading, buzzerLEDpin

    reading= board.sonar_read(triggerPin)#reads the value from the sensor
    time.sleep(0.5)#waits for 0.5 seconds
    
    if first_reading:
        first_reading = False  # Set the flag to False after the first reading

    if int(reading[0])>5:#if the cm readings is greater than 5cm
        board.digital_write(buzzerLEDpin,1)#turns on the buzzer and LED
    else:
        board.digital_pin_write(buzzerLEDpin,0)# buzzer and LED remain off

# Thermistor Callback Function

def process_thermistor_data(data): 
    """
    This function will parse the data from the thermistor and return a list of  average temperature values every second which can then be graphed

    INPUT: data: [pin_mode, pin, current_reported_value,  timestamp] {This is from the arduino}
    
    OUTPUT: A list of average temperature values every second {tempEverySecond}
    
    DEPENDENCIES: math, require 2 variables called tempData = [] and tempEverySecond = [] to be defined globally

    """
    #GLOBAL VARIABLES
    from polling_loop import tempEverySecond, tempData, rateOfChange

    # IMPORTS
    import math
    from pymata4 import pymata4

    rateOfChangeFactor = 5
    
    tempData.append([data[2]*(5/1023),data[3]]) # Taking the data that comes from the Arduino and then turning it into a resistance value based on the voltage divider calculation
    timeTaken = data[3] - tempData[0][1] # Calculating the time taken between most recent data point and the first data point in the list


    if int(timeTaken) >= 1:
        #calculating average voltage reading in V   
        sum = 0
        for data in tempData: #NOTE: Can we just use the sum function here?
            sum+=data[0]
        avgVoltage = (sum / len(tempData))

        #calculating resistance of thermistor via voltage divider in Kilo ohms
        resistance = ((5100*avgVoltage)/(5-avgVoltage))/1000
        
        #converting resistance to degrees celsius
        avgTemp = round((-21.21*math.log(resistance))+72.203, 2) 
        tempEverySecond.append(avgTemp)
        tempData.clear()
        if len(tempEverySecond) >= rateOfChangeFactor:
            roc = (tempEverySecond[-1]-tempEverySecond[-5])/rateOfChangeFactor
            rateOfChange.append(round(roc,3))
            
def process_ambThermistor_data(data): 
    """
    This function will parse the data from the thermistor and return a list of  average temperature values every second which can then be graphed

    INPUT: data: [pin_mode, pin, current_reported_value,  timestamp] {This is from the arduino}
    
    OUTPUT: A list of average ambient temperature values every second outside the room {tempEverySecond}
    
    DEPENDENCIES: math, require 2 variables called ambTempData = [] and ambTempEverySecond = [] to be defined globally

    """
    #GLOBAL VARIABLES
    from polling_loop import ambTempEverySecond, ambTempData

    # IMPORTS
    import math
    from pymata4 import pymata4
    
    ambTempData.append([data[2]*(5/1023),data[3]]) # Taking the data that comes from the Arduino and then turning it into a resistance value based on the voltage divider calculation
    timeTaken = data[3] - ambTempData[0][1] # Calculating the time taken between most recent data point and the first data point in the list


    if int(timeTaken) >= 1:
        #calculating average voltage reading in V   
        sum = 0
        for data in ambTempData: #NOTE: Can we just use the sum function here?
            sum+=data[0]
        avgVoltage = (sum / len(ambTempData))

        #calculating resistance of thermistor via voltage divider in Kilo ohms
        resistance = ((5100*avgVoltage)/(5-avgVoltage))/1000
        
        #converting resistance to degrees celsius
        avgTemp = round((-21.21*math.log(resistance))+72.203, 2) 
        ambTempEverySecond.append(avgTemp)
        ambTempData.clear()

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
        

