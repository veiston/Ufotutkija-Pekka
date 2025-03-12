# snake_game.py
# Simple Snake game where the player earns money based on the snake's length.

import random
import curses
from Source.utilities import print_separator
from colorama import Fore, Style

def play_snake(player):
    """
    Classic Snake game where the player earns money based on how long they survive.
    """

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

    # Score system
    score = 0

    while True:
        stdscr.clear()
        stdscr.border()

        # Draw food
        stdscr.addch(food[0], food[1], "O")

        # Move snake
        new_head = [snake[0][0], snake[0][1]]

        if direction == curses.KEY_UP:
            new_head[0] -= 1
        elif direction == curses.KEY_DOWN:
            new_head[0] += 1
        elif direction == curses.KEY_LEFT:
            new_head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            new_head[1] += 1

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
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            direction = key

    # Calculate winnings
    winnings = bet + (score * 5)
    player["money"] += winnings

    print_separator()
    print(f"{Fore.GREEN}Game Over!{Style.RESET_ALL}")
    print(f"Snake length: {score + 1}")
    print(f"You won: ${winnings}")

def get_bet(player):
    """Asks the player for a bet before playing."""
    while True:
        print("\nEnter your bet amount or type 'exit' to leave:")
        bet_input = input("> ")
        if bet_input.lower() == "exit":
            return None

        try:
            bet = int(bet_input)
            if 10 <= bet <= player["money"]:
                return bet
            else:
                print(f"{Fore.RED}Invalid bet. Enter an amount between $10 and ${player['money']}.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Invalid input. Enter a number.{Style.RESET_ALL}")
