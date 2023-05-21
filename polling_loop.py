# By Jayant Godse
# Date: 18/04/2023
"""
This program will outline how the arduino will continuosly read data from the sensors and then use that data to control other functions.

"""
# Import the required libraries
import time
from pymata4 import pymata4
from Menu import temp, tempData, tempEverySecond, rateOfChange, ambTempData, ambTempEverySecond
from callback_functions import process_thermistor_data, check_thermistor_operation, check_fan_operation, process_ambThermistor_data
from motor import control_motor


# Initialise the Arduino
board = pymata4.Pymata4()




# Callback data indices
callbackPinMode = 0
callbackPin = 1
callbackValue= 2
callbackTime = 3


# Initialise pins
thermistorPin = 1
ambientPin = 2
fanPin1 = 5
fanPin2 = 6
ledPin = 2





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
    # USE THE GLOBAL TEMP VALUE FROM THE MENU FILE
    global temp 
    global tempData
    global tempEverySecond
    global ambTempData
    global ambTempEverySecond
    global rateOfChange

    # =======================================
    # Polling Loop
    # =======================================

    # Check if all componenets are working
            
    check_thermistor_operation(thermistorPin)
    check_fan_operation(fanPin1, fanPin2)


    # Setup the pins
            
    board.set_pin_mode_analog_input(thermistorPin, process_thermistor_data)
    board.set_pin_mode_analog_input(ambientPin, process_ambThermistor_data)

    while True:
        try:
            # Make the loop sleep every second to get the time correct 
            # display.show_word("HI")

            time.sleep(1)

            # Start the timer
            
            startTime = time.time()
            

            # display.show_word("    ")


           
            # =======================================
            # MOTOR CONTROL
            # =======================================

            #airflow(q) = cubic feet per minute, i.e. cubic feet of room / number of airflows in and out of the room in a minute
            # heatflow (h) = airflow(q) * temp difference(delta T)
            #goal range = (23,27) --> goal temp is 25
           temp2 = ambTempEverySecond[-1]
            while True:
                try:
                    cubicFeet = int(input(("What is the volume of the room in feet? ")))
                    flows = float(input(("How many times would you like the air to flow in and out of the room per hour? ")))
                    airflow = (cubicFeet)*(flows)/(60)
                    current_temp = tempEverySecond[-1]
                    deltaTemp = float(current_temp - temp2)
                     h = (airflow)*(deltaTemp)
                    if cubicFeet > 0:
                        if flows > 0:
                            break
                    else:
                        print("Enter valid response")
                except keyboardInterrupt
                    quit()
                    
            # if heatflow is less than 0, this means the current temp is lower than goal
            # if heatflow is gteater than 0, this means the current temp is greater than goal
            
            if len(tempEverySecond) >= 1 and len(ambTempEverySecond) >= 1
                current_temp = tempEverySecond[-1]
                      if h > 0:
                        direction = 'clockwise'
                             if 0 < h <= 0.10:
                                speed = 100
                            elif 0.10 < h <= 0.50:
                                speed = 120
                            elif 0.50< h <= 1.00:
                                speed = 150
                            elif 1.00 < h <= 2.00
                                speed = 200
                            elif h > 2.00:
                                speed = 250
                    elif h < 0:
                        direction= 'anticlockwise'
                            if -0.10 <= h < 0:
                                speed = 100
                            elif -0.50 <= h < -0.10:
                                speed = 120
                            elif -1.00<= h < -0.50:
                                speed = 150
                            elif -2.00 <= h < -1.00
                                speed = 200
                            elif h < -2.00:
                                speed = 250
                    else:
                        direction = 'clockwise'
                        speed = 0
                    
                control_motor(direction,speed)


            # End the timer
            
            endTime = time.time()

            # Calculate the cycle length
            
            cycleLength = polling_loop_cycle_length(startTime, endTime)

            # =======================================
            # PRINT STATEMENTS
            # =======================================
          
            print(f"Cycle Length: {cycleLength} seconds")
            if len(tempEverySecond)>=1:
                print(f"Temperature: {tempEverySecond[-1]}°C") # The tempEverySecond variable is somehow auto exported from the callback function.
            if len(ambTempEverySecond)>=1:
                print(f"Ambient Temperature: {ambTempEverySecond[-1]}°C")
            if len(rateOfChange)>=1:    
                print(f"Rate of Change: {rateOfChange[-1]}°C/time")
                if abs(rateOfChange[-1]) > 5:
                    if rateOfChange[-1] > 0:
                        print('!WARNING! Temperature is rapidly increasing')
                    elif rateOfChange[-1] < 0:
                        print('!WARNING! Temperature is rapidly decreasing') 
                      
            # Return the data to the main menu

            returnData = [tempEverySecond, cycleLength, rateOfChange, ambTempEverySecond]
            
        except KeyboardInterrupt:
            control_motor()
            return returnData
            

# Polling Loop

if __name__ == "__main__":

    polling_loop()
