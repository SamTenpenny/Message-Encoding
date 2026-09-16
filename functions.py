import string
import sys
import subprocess
import time
from pathlib import Path
import random

home_dir = Path.home()
path_to_file = home_dir / "Desktop" / "encoded_file.txt"

# Display menu to user
def display_menu():
  print("1. Encode a message (Will overwrite existing file)")
  print("2. Append encoded message (Will add to existing file)")
  print("3. Decode encoded message file")
  print("4. Display Menu")
  print("5. Exit")


# Handle choice of user and direction of program
def choice_handler():
  choice = int(input("Please select an option from the menu: "))
  return choice


# Encode message with offset value
def encode_message():
  message = input("Enter message to encode: ")
  offset = random.randint(1, 25)
  print("\nMessage encoded with random offset.")
  time.sleep(2)
  clear_screen()
  encoded_message = []
  encoded_message.append(f"{offset}: ")
  
  for c in message:
    if c.islower():
      index = string.ascii_lowercase.index(c)
      encoded_message.append(string.ascii_lowercase[(index - offset) % 26])
    elif c.isupper():
      index = string.ascii_uppercase.index(c)
      encoded_message.append(string.ascii_uppercase[(index - offset) % 26])
    else:
      encoded_message.append(c)

  return "".join(encoded_message)


# Decode selected message with correct offset value
def decode_message(encoded_file):
  parsed_file = parse_encoded_file(encoded_file)
  messages = parsed_file[1]
  offsets = parsed_file[0]
  decoded_messages = []

  for offset, message in zip(offsets, messages):
    decoded_message = []
    for c in message:
      if c.islower():
        index = string.ascii_lowercase.index(c)
        decoded_message.append(string.ascii_lowercase[(index + offset) % 26])
      elif c.isupper():
        index = string.ascii_uppercase.index(c)
        decoded_message.append(string.ascii_uppercase[(index + offset) % 26])
      else:
        decoded_message.append(c)
    decoded_messages.append("".join(decoded_message))

  return "\n".join(decoded_messages)


# Create encoded message with offset and write to .txt file
def write_encoded_to_file(file_path, message):
  with open(file_path, "w") as f:
    f.write(message + "\n")

# Update message to encoded file with append
def edit_encoded_file(file_path, message):
  with open(file_path, "a") as f:
      f.write(message + "\n")


# Use written file to decode message with read
def read_encoded_file(file_path):
  with open(file_path) as f:
    file_message = f.read()
    return file_message


# Parse encoded lines for offset and message
def parse_encoded_file(file_message):
  message_file_split = file_message.splitlines()
  message_list = []
  offset_list = []

  for lines in message_file_split:
    messages = lines.split(": ", 1)
    message_list.append(messages[1])
    offset_list.append(int(messages[0]))
  
  return offset_list, message_list


# Used to clear screen of too much text
def clear_screen():
    if sys.platform == 'win32':
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)
