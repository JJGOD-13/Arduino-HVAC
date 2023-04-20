temp = 25

def main_menu():
    try:
        while True:
            #loop back to the main menu unless exited
            print("-----------------", '\033[1m' + "    Main Menu    " + '\033[0m', "-----------------", 
                "1: Fan Operation",
                "2: Graphing",
                "3: System Settings", 
                "4: Exit", "", sep="\n")
            
            #verify input
            operation = input("Enter value: ")
            while True:
                if operation == "1" or operation == "2" or operation == "3" or operation == "4":
                    break
                else:
                    operation = input("Enter a valid input (1, 2, 3 or 4): ")
            

            #operation 1: Fan operations
            if operation == "1":
                #start polling loop
                pass

            #operation 2: Graphing
            elif operation == "2":
                #graphing function
                pass

            #operation 3: System settings
            elif operation == "3":
                #pin function
                global temp
                while True:
                    x = input(f"The current temperature is set to {temp} degrees celcius. Enter the new temperature value: ")
                    try: 
                        temp = int(x)
                        if int(temp) == float(temp) and 15<=temp<=30:
                            break
                        else:
                            print("Please enter a positive integer value between 15 and 30.\n")
                    except:
                        print("Please enter a valid integer value between 15 and 30.\n")
                print(f"The new temperature is {temp} degrees celcius. \n")
                while True:
                    x = input("Would you like to return to the Main Menu (y/n): ")
                    if x == "y" or x == "n":
                        break
                    else:
                        print("Invalid input. Please try again.")
                if x == "y":
                    print("\nReturning to main menu... \n")
                else:
                    print("\nExiting...\n")
                    break

            elif operation == "4":
                break
    except KeyboardInterrupt:
        print("\nExiting...\n")
        print(5*"\n")
        print("You have exited the program")
        print("\n")
        exit(0)
        


def system_settings():
    print(temp)

if __name__ == "__main__":
    main_menu()
    system_settings()

