"""
This file contains the graph() function that generates a graph of temperature against time and the randomised_data() function that adds a randomised temperature value to a data list
"""
import matplotlib.pyplot as plt
import random
import time

def graph(temperatureValues: list):
    """
    This function generates a graph that plots temperature against time for the last 20s

    :param temperatureValues: a list of temperature values to be plotted (1 value/second)

    :return: None
    """
    timeValues = []
    for n in range(1,21):
        timeValues.append(n)

    valuesToBeGraphed = temperatureValues[-20:]

    plt.plot(timeValues,valuesToBeGraphed)
    plt.xlabel('Time(s)')
    plt.ylabel('Temperature(°C)')
    plt.title('Temperature vs Time')
    plt.show()

def randomised_data(data: list)-> list:
    """
    This function will generate a pseudo-random number and add it to a list of data for graphing.
    
    :param data: current list of values to be appended to
    
    :return: new list of data with added value
    """
    increment = random.random()*0.1
          
    if random.random()<0.25: #less likelihood for temperature to stop increasing/decreasing and start decreasing/increasing
        if increasing == True:
            data.append(data[-1]-increment)
            increasing = False
        elif increasing == False:
            data.append(data[-1]+increment)
            increasing = True
    else:
        if increasing == True:
            data.append(data[-1]+increment)
        elif increasing == False:
            data.append(data[-1]-increment)

    return data


if __name__ == '__main__':
    try:
        #need to initialise as global variables
        data = [22] 
        increasing = random.choice([True,False])
            
        while True:
            time.sleep(1)
            randomised_data(data)
    except KeyboardInterrupt:
        graph(randomised_data(data))
