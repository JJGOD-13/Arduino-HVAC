from pymata4 import pymata4


fanPin1 = 5 #pwm
fanPin2 = 6 #pwm

board_motor = pymata4.Pymata4()

board_motor.set_pin_mode_pwm_output(fanPin1)
board_motor.set_pin_mode_pwm_output(fanPin2)

def control_motor(board,direction = 'clockwise',speed = 0): 
    """
    This function turns on the motor to a given speed and direction

    :Param direction: string that is either 'clockwise' or 'anticlockwise'
    :Param speed: integer between 100 and 255
    :return: None
    """
    if direction == 'clockwise':
        board.pwm_write(fanPin1,speed)
        board.pwm_write(fanPin2,0)
    if direction == 'anticlockwise':
        board.pwm_write(fanPin1,speed)
        board.pwm_write(fanPin2,0)


            
