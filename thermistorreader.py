from pymata4 import pymata4
import time
from matplotlib import pyplot as plt
import math

# Define board and variables
board = pymata4.Pymata4()
thermistorPin = 1 # Analog Pin
pollTime = 1

# Global Variable 
tempData = []
tempEverySecond = []




def process_thermistor_data(data): 
    """
    A callback function to report data changes.
    :param data: [pin_mode, pin, current_reported_value,  timestamp] 
    """
    tempData.append([data[2],data[3]]) # data is the Raw data from Thermistor
    timeTaken = data[3] - tempData[0][1]
    

    if int(timeTaken) >= 1:
        avgTemp = sum(tempData[0]) / len(tempData)
        avgTemp = round((-2*math.log(avgTemp/100))+42.203, 2) # Well this is completley useless. No clue how to make this work 
        print(f'value = {tempData[-1][0]}, time = {round(timeTaken, 2)}, avgTemp = {avgTemp}')
        tempEverySecond.append(avgTemp)
        tempData.clear()



def main():   
    board.set_pin_mode_analog_input(thermistorPin, process_thermistor_data)
    
    # Main loop:
    print("Starting polling loop")
    while True:
        try:
            time.sleep(pollTime) 
            
            
        except KeyboardInterrupt:
            plt.plot(tempEverySecond)
            plt.xlabel('Time(s)')
            plt.ylabel('Temperature(°C)')
            plt.title('Temperature vs Time')
            
            plt.show()
            board.shutdown()
            break
            
            

if __name__ == "__main__":
    main()