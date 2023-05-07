"""
This file contains the control_motor function that is used to control whether the fan spins clockwise or anticlockwise.

"""


def control_motor(direction = 'clockwise',speed = 0): 
    """
    This function turns on the motor to a given speed and direction

    :Param direction: string that is either 'clockwise' or 'anticlockwise'
    :Param speed: integer between 100 and 255
    :return: None
    """
    from polling_loop import board,fanPin1,fanPin2


    board.set_pin_mode_pwm_output(fanPin1)
    board.set_pin_mode_pwm_output(fanPin2)

    if direction == 'clockwise':
        board.pwm_write(fanPin1,speed)
        board.pwm_write(fanPin2,0)
    if direction == 'anticlockwise':
        board.pwm_write(fanPin1,speed)
        board.pwm_write(fanPin2,0)


            
