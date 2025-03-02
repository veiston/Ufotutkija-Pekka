# shop.py

from colorama import Fore, Style
from utilities import print_separator
from items import items

def shop():
    print_separator()

    # TODO !SONA ALREADY HAS AN IMPLEMENTATION OF STORE! replace this stub with actual code about shoping and gambling
    print("There will be a store, but for now you get an old Nokia for free")
    print("\nHere is also a list of potentially (in future) reachable items from 'items' list: ")

    for item in items.values():
        print(f"-{item['name']} "
              f"({Fore.MAGENTA}${item['price']}{Style.RESET_ALL}, "
              f"Success chance: {Fore.GREEN}{item['success_chance']}%{Style.RESET_ALL})")