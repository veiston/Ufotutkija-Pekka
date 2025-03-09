# utilities.py

import time
import sys

def type_writer(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_separator():
    print("\n" + "=" * 50 + "\n")

def input_press_enter(prompt):
    while True:
        key = input(prompt)
        if key == "":
            break

def input_integer(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print('Dude, there are no such options here, try again')