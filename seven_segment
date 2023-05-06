from pymata4 import pymata4
import time
board=pymata4.Pymata4()

segPins=[3,4,5,6,7,8,9,10,11,12,13]
for pin in segPins:
    board.set_pin_mode_digital_output(pin)

def seven_segment(message):
    """ 
    This function will print an alphanumeric message onto the seven segment display.
    Input: alphanumberic message
    """
    numPins=[3,4,5,6,7,8,9]
    alphanumericDictionary = {
        
        "1":[0,1,1,0,0,0,0],
        "":[0,0,0,0,0,0,0],
        " ":[0,0,0,0,0,0,0],
        "a":[1,1,1,0,1,1,1],
        "b":[0,0,1,1,1,1,1],
        "d":[0,1,1,1,1,0,1],
        "e":[1,0,0,1,1,1,1],
        "f":[1,0,0,0,1,1,1],
        "g":[1,1,1,1,0,1,1],
        "h":[0,1,1,0,1,1,1],
        "i":[0,1,1,0,0,0,0],
        "l":[0,0,0,1,1,1,0],
        "n":[0,0,1,0,1,0,1],
        "o":[0,0,1,1,1,0,1],
        "p":[1,1,0,0,1,1,1],
        "r":[0,0,0,0,1,0,1],
        "s":[1,0,1,1,0,1,1],
        "t":[0,0,0,1,1,1,1],
        "u":[0,0,1,1,1,0,0]
                              
                              }
    messageList=[]
    for j in message:
        messageList.append(j) 
    for k in range(0,5):
        messageList.append("")

    for l in range(0,len(messageList)-4):
        x=time.time()
        while True:
            for i in range(0,len(numPins)):
                board.digital_write(numPins[i],0)
            board.digital_write(10,0)
            board.digital_write(11,1)
            board.digital_write(12,1)
            board.digital_write(13,1)
            digit1=str(messageList[0])
            for i in range(0,7):
                board.digital_write(numPins[i],alphanumericDictionary[digit1][i])
            
            for i in range(0,len(numPins)):
                board.digital_write(numPins[i],0)
            board.digital_write(10,1)
            board.digital_write(11,0)
            board.digital_write(12,1)
            board.digital_write(13,1)
            digit2=str(messageList[1])
            for i in range(0,7):
                board.digital_write(numPins[i],alphanumericDictionary[digit2][i])
        
            for i in range(0,len(numPins)):
                board.digital_write(numPins[i],0)
            board.digital_write(10,1)
            board.digital_write(11,1)
            board.digital_write(12,0)
            board.digital_write(13,1)
            digit3=str(messageList[2])
            for i in range(0,7):
                board.digital_write(numPins[i],alphanumericDictionary[digit3][i])
            
            for i in range(0,len(numPins)):
                board.digital_write(numPins[i],0)
            board.digital_write(10,1)
            board.digital_write(11,1)
            board.digital_write(12,1)
            board.digital_write(13,0)
            digit4=str(messageList[3])
            for i in range(0,7):
                board.digital_write(numPins[i],alphanumericDictionary[digit4][i])

            y=time.time()
            if y-x>1:
                messageList.pop(0)
                break
            

try:
    seven_segment("beginning polling loop")
except KeyboardInterrupt:
    board.shutdown()
    exit()


