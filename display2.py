"""
A more imporved version of the display.py file. 

This version will utilize 2 shift registers and will also  be able to scroll chars across the display.
"""
from pymata4 import pymata4
board = pymata4.Pymata4()

# PINS

latchPin = 8
clockPin = 9
dataPin = 10

"""
- Compared to the previous version this version will only requrire 3 pins in order to be used properly. 
- The use of the display pins will be removed as the shift registers will be used to control the display.
- This will require me to append the display values at the end of the list of values that show the char on the disp.
- 
"""


# =======================================
# DICTIONARIES
# =======================================

chars = {
    "key" : ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "O", "P", "S", "T", "U", "Y", "Z", " "],

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



# =======================================
# DISPLAY DICTIONARY
# =======================================

"""
- This dictionary will contain lists of 0's and 1's which will have to be appended to the char list.
- This should let control which display a char is shown on.
"""
displays = {

    1 : [0,0,0,1],
    2 : [0,0,1,0],
    3 : [0,1,0,0],
    4 : [1,0,0,0]
}

# =======================================
# FUNCTIONS
# =======================================

def show_char(char, display):
    """
    This function will take in a char and display and will show the char on the display.
    """
    # from polling_loop import board
    # board = pymata4.Pymata4()
    # cast the char to string
    char = str(char)
    # Get the char from the chars dictionary
    char = chars[char]

    # Get the display from the displays dictionary
    display = displays[display]
    display.reverse()
    

    # cast the char to list
    char = list(char)

    # Reverse the list
    char.reverse()

    # Append the display to the end of the char list
    for i in range(len(display)):
        char.append(display[i])

    # Also need to add on a list of 0's to the end of the list so that it doesn't mess with the next char we show.
    for i in range (4):
        char.append(0)

    # Reverse the list back to original order

    
    char = list(char)

    # load the char onto the display
     # Loop through the binary representation
    for j in range(len(char)):
        # Set the data pin to the current bit
        board.digital_write(dataPin, char[j])

        # Pulse the clock pin
        board.digital_write(clockPin, 1)
        board.digital_write(clockPin, 0)
    board.digital_write(latchPin, 1)
    board.digital_write(latchPin, 0)
    print(char)

def show_word(word):
    """
    This function will take in a word/number and will show the word on the display.
    """
    import time
    #cast the word to string
    word = str(word)
    word.upper()

    # cast the word to list

    word = list(word)

    for i in range(len(word)):
        show_char(word[i], i+1)
        time.sleep(0.1)
    
        

            
def clear_display():
    """
    This function will clear the display.
    """
    # from polling_loop import board
    
    # Loop through the binary representation
    for j in range(16):
        # Set the data pin to the current bit
        board.digital_write(dataPin, 0)

        # Pulse the clock pin
        board.digital_write(clockPin, 1)
        board.digital_write(clockPin, 0)
    board.digital_write(latchPin, 1)
    board.digital_write(latchPin, 0)


if __name__ == "__main__":
    clear_display()
    show_char("A", 1)
