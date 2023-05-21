from pymata4 import pymata4
import time

def object_detection_mode():
    """ 
    uses ultrasonic sensor to detect objects. if it senses an object greater than 4cm away, 
    it will flash a blue light with a frequency of 1hertz and beep continously.
    """
    board = pymata4.Pymata4()
    triggerPin = 8
    echoPin = 9
    buzzerpin=7
    first_reading = True # Flag to indicate first reading

    while True:
        try:
            board.set_pin_mode_sonar(triggerPin, echoPin, timeout=200000)#sets the pins for the sensor
            board.set_pin_mode_digital_output(buzzerpin)#sets digital input
            reading=board.sonar_read(triggerPin)#reads the value from the sensor
            time.sleep(0.5)#waits for 0.5 seconds
            
            if first_reading:
                first_reading = False  # Set the flag to False after the first reading
                continue

            if int(reading[0])>5:#if the cm readings is greater than 5cm
                board.digital_write(buzzerpin,1)#turns on the buzzer and LED
            else:
                board.digital_pin_write(buzzerpin,0)# buzzer and LED remain off

        except KeyboardInterrupt:
            board.shutdown()
            quit()




object_detection_mode()