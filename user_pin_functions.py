# Author: Jayant Godse
# Date: 18/04/2023
# THis file contains the function for setting up the user pin and changing it.

import csv
import time

    

# Global Variables

def setup_user_pin():
        """
        This function will set the user pin
        INPUTS: None
        OUTPUTS: True if the user hasn't set their pin before, False if they have
        DEPENDENCIES: Requires a csv file called passcodes.csv
        """
        # Open the csv file and then set userPin and specialPin
        with open("passcodes.csv") as file:
            reader = csv.DictReader(file)
            row = list(reader)
            userPin = row[0]["Value"]
            specialPin = row[1]["Value"]

        
    
        # If this is the first time that the user has run the program, show the welcome message
        print(4*"\n")
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
            setup_user_pin()

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
        file.close()
        
        
        




def check_user_pin():
    """
    This function will check the user pin
    INPUT: None
    OUTPUT: True if the pin is correct, (1 if the special pin is entered)
    DEPENDENCY: Requires a csv file called passcodes.csv to exist. 
                Requires csv module imported.

   
    """
    # set the incorrect pin count to 0
    incorrectPinCount = 0
    # Use the global variable for the user pin
    
    # Open the csv file and then read the data
    
    with open("passcodes.csv") as file:
        reader = csv.DictReader(file)
        row = list(reader)
        userPin = row[0]["Value"]
        specialPin = row[1]["Value"]
        

    if  int(str(userPin)) == 0:
        return False
        
    while True:
        try:
            with open("passcodes.csv") as file:
                reader = csv.DictReader(file)
                row = list(reader)
                userPin = row[0]["Value"]
                specialPin = row[1]["Value"]

            if incorrectPinCount == 3: # Might need to put in a different function i.e shutdown() if this is the case #TODO
                print("You have entered the incorrect pin 3 times")
                time.sleep(0.2)
                print("The system will now shut down")
                time.sleep(0.2)
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
            if int(tempPin) == int(userPin):
                return True
                

            if int(tempPin) == int(specialPin):
                print('\033[1;32;40m' + "You have entered the special pin" + '\033[0m')
                # Easter Egg
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
    check_user_pin()
    
