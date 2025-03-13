# snake_game.py
# Simple Snake game where the player earns money based on the snake's length.

import random
import curses
from utilities import print_separator, input_integer, clear_screen
from colorama import Fore, Style
from player import get_current_player

def play_snake(player):
    """
    Classic Snake game where the player earns money based on how long they survive.
    """
    clear_screen()
    print_separator()
    print(f"{Fore.YELLOW}Welcome to Snake!{Style.RESET_ALL}")
    print(f"Your current balance: {Fore.GREEN}${player['money']}{Style.RESET_ALL}")

    # Ask the player for a bet
    bet = get_bet(player)
    if bet is None:
        return  # Player canceled

    # Initialize the game screen
    curses.wrapper(lambda stdscr: run_snake_game(stdscr, player, bet))

def run_snake_game(stdscr, player, bet):
    clear_screen()
    """Runs the Snake game inside a curses window."""
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)  # Snake speed

    # Screen size
    sh, sw = stdscr.getmaxyx()
    w, h = sw - 2, sh - 2

    # Snake initial position
    snake = [[sh // 2, sw // 2]]
    food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
    direction = curses.KEY_RIGHT

    # Mapping of direction keys to coordinate changes
    key_delta = {
        curses.KEY_UP: (-1, 0),
        curses.KEY_DOWN: (1, 0),
        curses.KEY_LEFT: (0, -1),
        curses.KEY_RIGHT: (0, 1)
    }

    # Score system
    score = 0

    while True:
        stdscr.clear()
        stdscr.border()

        # Draw food
        stdscr.addch(food[0], food[1], "O")

        # Move snake using mapping
        dx, dy = key_delta.get(direction, (0, 0))
        new_head = [snake[0][0] + dx, snake[0][1] + dy]

        # Check for collisions
        if new_head in snake or new_head[0] == 0 or new_head[0] == h or new_head[1] == 0 or new_head[1] == w:
            break  # Game over

        snake.insert(0, new_head)

        # Check if snake eats food
        if new_head == food:
            score += 1
            food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
        else:
            snake.pop()

        # Draw snake
        for segment in snake:
            stdscr.addch(segment[0], segment[1], "#")

        stdscr.refresh()

        # Get new direction from user
        key = stdscr.getch()
        if key in key_delta:
            direction = key

    # Calculate winnings
    score = score * 5
    winnings = bet + (score)
    player["money"] += winnings

    print_separator()
    print(f"{Fore.GREEN}Game Over!{Style.RESET_ALL}")
    print(f"Snake length: {score + 1}")
    print(f"You won: {Fore.GREEN}${score}{Style.RESET_ALL}")
    return player["money"]

def get_bet(player):
    """Asks the player for a bet before playing. Type 'exit' to cancel."""
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
    play_snake(get_current_player())