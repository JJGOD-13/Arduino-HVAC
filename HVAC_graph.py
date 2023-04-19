import matplotlib.pyplot as plt
import random
import time

def graph(temperatureValues: list):
    timeValues = []
    for n in range(1,21):
        timeValues.append(n)

    plt.plot(timeValues,temperatureValues)
    plt.xlabel('Time(s)')
    plt.ylabel('Temperature(°C)')
    plt.title('Temperature vs Time')
    plt.axis([0,21,min(temperatureValues)-3,max(temperatureValues)+3])
    plt.show()

def randomised_data():
    data = [22]
    increasing = True
    while len(data)<20:
        increment = random.random()   
        if random.random()<0.25:
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

if __name__ == "__main__":
    graph(randomised_data())


# while len(temperatureValues)==20:
#     increment = random.random()
#     if random.random()<0.5:
#         temperatureValues.append(temperatureValues[-1]+increment)
#     else:
#         temperatureValues.append(temperatureValues[-1]-increment)
#     temperatureValues.pop(0)
#     print(temperatureValues)
#     time.sleep(1)

