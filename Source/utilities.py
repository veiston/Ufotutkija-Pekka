# utilities.py

import time
import sys
import os

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

def yes_no(prompt):
    while True:
        user_input = input(prompt)
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print('Dude, there are no such options here, try again')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def waiting_action():
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(1)
