from pymata4 import pymata4


in1 = 9 #pwm
in2 = 10 #pwm

board_motor = pymata4.Pymata4()

board_motor.set_pin_mode_pwm_output(in1)
board_motor.set_pin_mode_pwm_output(in2)

def control_motor(direction,speed): 
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
        board_motor.digital_write(in1,speed)
        board_motor.digital_write(in2,0)

def turn_motor_off():
    board_motor.digital_write(in1,0)
    board_motor.digital_write(in2,0)

            
