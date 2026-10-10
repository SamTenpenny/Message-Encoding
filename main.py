# Imports functions from our functions module we created or from python supplied modules
from msg_enc_func import display_menu, choice_handler, encode_message, decode_message, write_encoded_to_file, edit_encoded_file, read_encoded_file, clear_screen, keystroke, path_to_file
import time
import sys

# Run the main program with all functions and imports integrated inside the main scope
def main():
    # While True remains True, continue running the program loop until False or System Exit
    while True:
        try:
            # Function creates a fresh terminal screen for reading
            clear_screen()
            
            # Display menu of options for user to select from
            display_menu()
            
            # Grab the menu option from user input 
            choice = choice_handler()

            # Option one runs function to recieve user message input, encode message user wrote, create text file, and then write encoded message to the file
            if choice == 1:
                write_encoded_to_file(path_to_file, encode_message())
            # Option two runs the same encoding function, but instead of using write to create a new text file it appends an updated message to the file
            elif choice == 2:
                edit_encoded_file(path_to_file, encode_message())
            # Option three will run the decode function. For each line of messages in the file it will decode and output them into the terminal without saving to a new file. This is a security measure.
            elif choice == 3:
                clear_screen()
                print(decode_message(read_encoded_file(path_to_file)))
                print("\nPress enter to return to the menu.")
                while True:
                    key = keystroke()
                    if key == "\r":
                        break
                    else:
                        print("Press enter to return to the menu.")
            # Option four is simply to display the menu again if it gets lost in too much text or clear screen does not run properly
            elif choice == 4:
                display_menu()
            # Option five will gracefully exit the program when the user is finished
            elif choice == 5:
                print("Exiting Program...")
                time.sleep(2)
                sys.exit()
            else:
                # Error handling or any numbers outside of the acceptable range
                print("Please select a number between 1-5")
        # Error handling for any inputs that are not integers of base 10
        except ValueError:
            print("Please select a number between 1-5")
        # Error handling if the file has any messages that are missing decode number assignment or missing a message entirely to decode
        except IndexError as e:
            e = f"\nMessage: Your file has encountered an error \nError: a line is Missing numerical assignment or message\n"
            print(e)
            time.sleep(5)


# Checks if file name is named main, it will proceed with running the main function
if __name__ == "__main__":
    main()