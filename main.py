from functions import display_menu, choice_handler, encode_message, decode_message, write_encoded_to_file, edit_encoded_file, read_encoded_file, clear_screen, path_to_file
import time
import sys
from msvcrt import getch as keystroke

def main():

    while True:
        try:
            clear_screen()
            display_menu()
            choice = choice_handler()

            if choice == 1:
                write_encoded_to_file(path_to_file, encode_message())
            elif choice == 2:
                edit_encoded_file(path_to_file, encode_message())
            elif choice == 3:
                clear_screen()
                print(decode_message(read_encoded_file(path_to_file)))
                print("\nPress enter to return to the menu.")
                while True:
                    if keystroke() == b"\r":
                        break
                    else:
                        print("Press enter to return to the menu.")
            elif choice == 4:
                display_menu()
            elif choice == 5:
                print("Exiting Program...")
                time.sleep(2)
                sys.exit()
            else:
                print("Please select a number between 1-5")
        except ValueError:
            print("Please select a number between 1-5")
        except IndexError as e:
            e = f"\nMessage: Your file has encountered an error \nError: a line is Missing numerical assignment or message\n"
            print(e)
            time.sleep(5)


if __name__ == "__main__":
    main()