from pymata4 import pymata4


fanPin1 = 5 #pwm
fanPin2 = 6 #pwm

board_motor = pymata4.Pymata4()

board_motor.set_pin_mode_pwm_output(in1)
board_motor.set_pin_mode_pwm_output(in2)

def control_motor(direction = 'clockwise',speed = 0): 
    """
    This function turns on the motor to a given speed and direction

    :Param direction: string that is either 'clockwise' or 'anticlockwise'
    :Param speed: integer between 100 and 255
    :return: None
    """
    if direction == 'clockwise':
        board_motor.pwm_write(in1,speed)
        board_motor.pwm_write(in2,0)
    if direction == 'anticlockwise':
        board_motor.pwm_write(in1,speed)
        board_motor.pwm_write(in2,0)


            
