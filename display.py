"""
VERSION: 1.0.0

This file will house the functions that are requried to display the data on the 7 segment display.
It will make use of the ability of shift registers in order to do this.
"""

from pymata4 import pymata4
import time

# PINS

latchPin = 8
clockPin = 9
dataPin = 10

display1 = 3
display2 = 4
display3 = 5
display4 = 6




"""
A dictionary of letters. 

There are letters that cannot be displayed
these are:
    K, M, N, Q, R, T, W, V,  X, Y, Z
"""

chars = {
        "key"   : ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "O", "P", "S", "T", "U", "Y", "Z", " "],

        "A" : [0, 1, 1, 1, 0, 1, 1, 1],
        "B" : [0, 1, 1, 1, 1, 1, 0, 0],
        "C" : [0, 0, 1, 1, 1, 0, 0, 1],
        "D" : [0, 1, 0, 1, 1, 1, 1, 0],
        "E" : [0, 1, 1, 1, 1, 0, 0, 1],
        "F" : [0, 1, 1, 1, 0, 0, 0, 1],
        "G" : [0, 0, 1, 1, 1, 1, 0, 1],
        "H" : [0, 1, 1, 1, 0, 1, 1, 0],
        "I" : [0, 0, 0, 0, 0, 1, 1, 0],
        "J" : [0, 0, 0, 0, 1, 1, 1, 0],
        "L" : [0, 0, 1, 1, 1, 0, 0, 0],
        "O" : [0, 0, 1, 1, 1, 1, 1, 1],
        "P" : [0, 1, 1, 1, 0, 0, 1, 1],
        "S" : [0, 1, 1, 0, 1, 1, 0, 1],
        "T" : [0, 1, 1, 1, 1, 0, 0, 0],
        "U" : [0, 0, 1, 1, 1, 1, 1, 0],
        "Y" : [0, 1, 1, 0, 1, 1, 1, 0],
        "Z" : [0, 1, 0, 1, 1, 0, 1, 1],
        " " : [0, 0, 0, 0, 0, 0, 0, 0],

    }

numbers = {
     
        "0" : [0, 0, 1, 1, 1, 1, 1, 1],
        "1" : [0, 0, 0, 0, 0, 1, 1, 0],
        "2" : [0, 1, 0, 1, 1, 0, 1, 1],
        "3" : [0, 1, 0, 0, 1, 1, 1, 1],
        "4" : [0, 1, 1, 0, 0, 1, 1, 0],
        "5" : [0, 1, 1, 0, 1, 1, 0, 1],
        "6" : [0, 1, 1, 1, 1, 1, 0, 1],
        "7" : [0, 0, 0, 0, 0, 1, 1, 1],
        "8" : [0, 1, 1, 1, 1, 1, 1, 1],
        "9" : [0, 1, 1, 0, 1, 1, 1, 1],

    }

# Create a pymata4 instance
board = pymata4.Pymata4()

# Set the pin modes
board.set_pin_mode_digital_output(latchPin)
board.set_pin_mode_digital_output(clockPin)
board.set_pin_mode_digital_output(dataPin)
board.set_pin_mode_digital_output(display1)
board.set_pin_mode_digital_output(display2)
board.set_pin_mode_digital_output(display3)
board.set_pin_mode_digital_output(display4)



def print_number_1to10():
    """
    This function will print the numbers 1 to 10 on the 7 segment display
    """
    keys = chars["key"]

    # Loop through the numbers 1 to 10
    for i in range(len(keys)):

        # Get the binary representation of the number
        print(keys[i])
        binary = chars[keys[i]]
        

        # Loop through the binary representation
        for j in range(len(binary)):

            # Set the data pin to the current bit
            board.digital_write(dataPin, binary[j])
            

            # Pulse the clock pin
            board.digital_write(clockPin, 1)
            board.digital_write(clockPin, 0)

        # Pulse the latch pin
        board.digital_write(latchPin, 1)
        board.digital_write(latchPin, 0)
            

        # Wait 1 second
        time.sleep(1)
 

def print_number():
    number = chars["A"]

    for j in range(len(number)):

            # Set the data pin to the current bit
            board.digital_write(dataPin, number[j])
            print("count")

            # Pulse the clock pin
            board.digital_write(clockPin, 1)
            board.digital_write(clockPin, 0)

    # Pulse the latch pin
    board.digital_write(latchPin, 1)
    board.digital_write(latchPin, 0)



def show_char(char):
    """
    This function will show a character on the 7 segment display
    INPUT: char - the character to be displayed

    """

    # Check if the character is a number
    if char in numbers:
         printer = numbers[char]
    elif char in chars:
        printer = chars[char]
    else:
        print("Invalid character")
        print("Characters that cannot be displayed are:")
        print("K, M, N, Q, R, T, W, V, X, Y, Z")
        return False
    
    # Loop through the binary representation
    for j in range(len(printer)):
        # Set the data pin to the current bit
        board.digital_write(dataPin, printer[j])

        # Pulse the clock pin
        board.digital_write(clockPin, 1)
        board.digital_write(clockPin, 0)
    board.digital_write(latchPin, 1)
    board.digital_write(latchPin, 0)

def show_word(word):
    """
    This function will show a word on the 7 segment display
    INPUT: word - the word to be displayed
    """
    word.upper()
    # Loop through the characters in the word
    for i in range(len(word)):
        # Show the current character
        show_char(word[i])

        # Wait 1 second
        time.sleep(1)