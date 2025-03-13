# blackjack.py
# Simple Blackjack mini-game where the player tries to beat the dealer.

import random
import time
from colorama import Fore, Style
from utilities import print_separator, type_writer, input_integer, clear_screen
from player import get_current_player

def play_blackjack(player):
    """
    Simple Blackjack game where the player tries to get as close to 21 as possible without going over.
    """
    clear_screen()
    print_separator()
    print(f"{Fore.YELLOW}Welcome to Blackjack!{Style.RESET_ALL}")
    print(f"Your current balance: {Fore.GREEN}${player['money']}{Style.RESET_ALL}")

    # Player chooses bet amount
    bet = get_bet(player)
    if bet is None:
        return  # Player canceled

    # Deal initial cards
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    # Show initial hands
    print("\nYour cards:", format_hand(player_hand))
    print(f"Dealer's first card: {dealer_hand[0]}")

    # Player's turn
    while sum(player_hand) < 21:
        print("\nWhat do you want to do?")
        print("1. Hit (Take another card)")
        print("2. Stand (Keep your current hand)")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            player_hand.append(draw_card())
            print("\nYou drew:", player_hand[-1])
            print("Your total:", sum(player_hand))

            if sum(player_hand) > 21:
                print(f"{Fore.RED}Bust! You went over 21.{Style.RESET_ALL}")
                player["money"] -= bet
                return
        elif choice == "2":
            break
        else:
            print("Invalid choice, try again.")

    # Dealer's turn
    print("\nDealer reveals their hand:", format_hand(dealer_hand))
    while sum(dealer_hand) < 17:
        time.sleep(1)
        dealer_hand.append(draw_card())
        print("Dealer draws:", dealer_hand[-1])

    dealer_total = sum(dealer_hand)
    player_total = sum(player_hand)

    # Determine winner
    print("\nFinal Results:")
    print(f"Your total: {player_total}")
    print(f"Dealer's total: {dealer_total}")

    if dealer_total > 21 or player_total > dealer_total:
        player["money"] += bet
        print(f"{Fore.GREEN}You win!{Style.RESET_ALL} {Fore.GREEN}+${bet}{Style.RESET_ALL}")
        return player["money"]

    elif player_total == dealer_total:
        print(f"{Fore.YELLOW}It's a tie!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Dealer wins!{Style.RESET_ALL} {Fore.RED}-${bet}{Style.RESET_ALL}")
        player["money"] -= bet
        return player["money"]

##########################################################################################
# Helper functions

def draw_card():
    """Returns a random card value between 2 and 11."""
    return random.randint(2, 11)

def format_hand(hand):
    """Returns a formatted string of the player's hand."""
    return ", ".join(str(card) for card in hand) + f" (Total: {sum(hand)})"

def get_bet(player):
    """Asks the player for a bet and validates the input. Type 'exit' to cancel."""
    while True:
        user_input = input("\nEnter your bet amount (or type 'exit' to quit):\n")
        if user_input.lower() == "exit":
            return None  # Exit option chosen
        try:
            bet = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'exit'.")
            continue
        if 10 <= bet <= player["money"]:
            return bet
        else:
            print(f"{Fore.RED}Invalid bet. Enter an amount between $10 and ${player['money']}.{Style.RESET_ALL}")

if __name__ == "__main__":
    play_blackjack(get_current_player())