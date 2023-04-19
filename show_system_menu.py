# Author: Jayant Godse
# Date: 18/04/2023
# THis file contains the function for showing the system menu

# Global Variables

userPin = 0

specialPin = 69420

# Show System Menu
def show_system_menu():
    try:
    
        global userPin

        # Check if this is the first time that the user has run the program
        if  userPin == 0:
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
            
            # Some more messages
            print("Thank you for setting your pin")
            print("Remember you can change your pin at anytime through the settings menu \n")
            print("Please enter your pin to continue")
        
        # Ask the user to enter their pin
        incorrectPinCount = 0
        while True:
            try:
                if incorrectPinCount == 3:
                    print("You have entered the incorrect pin 3 times")
                    print("The system will now shut down")
                    print("Your Pin will be erased")
                    userPin = 0
                    exit(1)
                
                tempPin = int(input("Please enter your pin: "))
                if tempPin == userPin:
                    break

                elif tempPin == specialPin:
                    print("You have entered the special pin")
                    # show_special_message()
                    break
                else:
                    print("The entered pin is incorrect. Please try again \n")
                    incorrectPinCount += 1
                    continue
            except ValueError:
                print("The entered pin is incorrect. Please try again \n")
                incorrectPinCount += 1
                continue
        
        # Show the system menu
        print(4*"\n")
        print("Welcome to the Arduino HVAC System \n")
        print("Please select an option from the menu below \n")
        print("Do so by entering the corresponding number \n")


    except KeyboardInterrupt:
        print(5*"\n")
        print("You have exited the program")
        print("\n")
        exit(1)
            
if __name__ == "__main__":

    show_system_menu()