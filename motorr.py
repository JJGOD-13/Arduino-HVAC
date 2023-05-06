
from pymata4 import pymata4 
import time
from thermistorreader import tempEverySecond
from menu import temp


board = pymata4.Pymata4()
def control_motor():
    aveTemp = (sum(thermistorreader))/(len(thermistorreader))
    numPins = [5,6]
    for i in numPins:
        board.set_pin_mode_pwm_output(i)
    while True:
        try:
            if aveTemp < temp - 2:
                board.pwm(5,180)
                time.sleep(3)
                print("Temperature recorded is less than the goal, direction of fan is set to move heat into room")
            if temp -2 <= aveTemp <= temp + 2:
                board.pwm_write(5,0)
                board.pwm_write(6,0)
                time.sleep(3)
            if aveTemp >= temp + 2:
                board.pwm(6,180)
                time.sleep(3)
                print("Temperature recorded is more than the goal, direction of fan is set to move heat out of the room")
        except KeyboardInterrupt:
            board.shutdown
            quit()

    


