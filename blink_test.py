##Adapted from the Pymata4 Documentation
#Provided under GNU AFFERO GENERAL PUBLIC LICENSE

import time

from pymata4 import pymata4

"""
Setup a pin for digital output and output a signal
and toggle the pin. Do this 4 times.
"""

def blink(my_board, pin):
    """
    This function will to toggle a digital pin.
    :param my_board: an PymataExpress instance
    :param pin: pin to be controlled
    """

    # set the pin mode
    my_board.set_pin_mode_digital_output(pin)

    # toggle the pin 4 times and exit
    for x in range(4):
        print('ON')
        my_board.digital_write(pin, 1)
        time.sleep(1)
        print('OFF')
        my_board.digital_write(pin, 0)
        time.sleep(1)

    my_board.shutdown()
# parameters
DIGITAL_PIN = 13 # arduino pin number - internal LED

board = pymata4.Pymata4()
print("Starting Blink Program - Use Ctrl+C to Quit")
try:
    blink(board, DIGITAL_PIN)
except KeyboardInterrupt: # use Ctrl+C to quit
    board.shutdown()
    exit(0) 