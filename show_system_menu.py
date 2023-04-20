# Author: Jayant Godse
# Date: 18/04/2023
# THis file contains the function for showing the system menu

import csv

# Open the csv file and then read the data
with open("passcodes.csv") as file:
    reader = csv.DictReader(file)
    row = list(reader)
    userPin = row[0]["Value"]
    specialPin = row[1]["Value"]
    

# Global Variables

def setup_user_pin():
        """
        This function will set the user pin
        INPUTS: None
        OUTPUTS: True if the user hasn't set their pin before, False if they have
        """
     # Set the global variable userPin
        global userPin

        # Check if this is the first time that the user has run the program
        if  int(str(userPin)) == 0:
            # If this is the first time that the user has run the program, show the welcome message
            print(4*"\n")
            print("Welcome to the Arduino HVAC System \n")
            print("Please set your 4 digit pin \n")



            # Ask the user to set their pin
            while True:
                try:
                    userPin = int(input("Please enter your 4 digit pin: "))
                    
                    if len(str(userPin)) != 4:
                        print("Your pin must be 4 digits long", end="\n\n")
                        continue
                    else:
                        break
                        
                except ValueError:
                    print("Please enter a valid 4 digit pin",end="\n\n")
                    
                    continue
            
            # Make sure the user is happy with their pin
            print(2 * "\n")
            print(f"Your pin has been set to {userPin}")
            # if they aren't happy, ask them to set their pin again

            if input("Are you happy with this pin? y/n: ") == "n":
                print("Please set your pin again")
                show_system_menu()

            # Set the pin in the csv file

            with open("passcodes.csv") as file:
                reader = csv.DictReader(file)
                row = list(reader)
                row[0]["Value"] = userPin
                
                with open("passcodes.csv", "w") as file:
                    fieldnames = ["Passcode", "Value"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames )
                    writer.writeheader()
                    writer.writerow(row[0])
                    writer.writerow(row[1])


            # Some more messages
            
            print("Thank you for setting your pin")
            print("Remember you can change your pin at anytime through the settings menu \n")
            print("Please enter your pin to continue")
            return True
        else:
            return False

# Show System Menu
def show_system_menu():
    try:
       
        
        # Ask the user to enter their pin
        check_user_pin()

        

        
        # Show the system menu
        print(4*"\n")
        print("Welcome to the Arduino HVAC System \n")
        print("Please select an option from the menu below \n")
        print("Do so by entering the corresponding number \n")
    
        # Options
        print("1. Fan Operation")
        print("2. Graphs")
        print("3. Settings")

        # Ask user for input
        while True:
            try:
                userOption = int(input("Please enter your option: "))
                if userOption == 1:
                    print("Fan Operation")
                    #TODO: Add fan operation function
                    break
                elif userOption == 2:
                    print("Graphs")
                    #TODO: Add graphs function
                    break
                elif userOption == 3:
                    print("Settings")
                    #TODO: Add settings function
                    break
                else:
                    print("Please enter a valid option")
                    continue
            except ValueError:
                print("Please enter a valid option")
                continue

        



    except KeyboardInterrupt:
        print(5*"\n")
        print("You have exited the program")
        print("\n")
        exit(1)


"""
This function will check the user pin
INPUT: None
OUTPUT: True if the pin is correct, False if the pin is incorrect. (1 if the special pin is entered)

#TODO:
    - Add a shutdown function if the user enters the incorrect pin 3 times
    - Save the pin to another file so that it is saved even if the program is closed
"""
def check_user_pin():
    # set the incorrect pin count to 0
    incorrectPinCount = 0
    # Use the global variable for the user pin
    
    # Open the csv file and then read the data
    with open("passcodes.csv") as file:
        reader = csv.DictReader(file)
        row = list(reader)
        userPin = row[0]["Value"]
        specialPin = row[1]["Value"]
        
    while True:
        try:
            if incorrectPinCount == 3: # Might need to put in a different function i.e shutdown() if this is the case #TODO
                print("You have entered the incorrect pin 3 times")
                print("The system will now shut down")
                print("Your Pin will be erased")
                userPin = 0
                
                # Erase the pin
                with open("passcodes.csv") as file:
                    reader = csv.DictReader(file)
                    row = list(reader)
                    row[0]["Value"] = userPin
                
                    with open("passcodes.csv", "w") as file:
                        fieldnames = ["Passcode", "Value"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames )
                        writer.writeheader()
                        writer.writerow(row[0])
                        writer.writerow(row[1])
                exit(1)
            
            tempPin = int(input("Please enter your pin: "))
            if tempPin == userPin:
                return True
                

            elif tempPin == specialPin:
                print("You have entered the special pin")
                # show_special_message()
                return(1)

            else:
                print("The entered pin is incorrect. Please try again \n")
                incorrectPinCount += 1
                continue
        except ValueError:
            print("The entered pin is incorrect. Please try again \n")
            incorrectPinCount += 1
            continue


if __name__ == "__main__":
    setup_user_pin()

    check_user_pin()
    
