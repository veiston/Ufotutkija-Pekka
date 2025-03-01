import time
import colorama

delay = 3

print('Welcome Pekkka!')
print('This is a quick demo of our game showing a multiple choice q&a-style mechanic for the investagion section of the game.\n Very demo. Dont be harsh. :D')
time.sleep(delay)

print(colorama.Fore.RED + '\nIntroduction' + colorama.Style.RESET_ALL)
print('Under the crimson moon, I arrived at an abandoned field on the outskirts of a forgotten town. The air pulsed with a chilling, strange hum – a call from the unknown. As an experienced paranormal investigator, I had spent years chasing inexplicable whispers, but nothing could have prepared me for that night. A glowing, alien-like light emanated from the broken ruins, signaling the presence of a being beyond the bounds of this world. In that charged moment, as fear and determination intertwined, my journey into the heart of an otherworldly mystery began.')
time.sleep(delay)

print("\n\nWhat is your name?")
name = input()
print(f"\n\nWelcome, {name}! Are you ready to embark on an adventure? (Y/N)")
if input() == 'Y':
    print("\n\nGreat! The adventure begins now.")
else:
    print("\n\nNo worries, you can return to the adventure later.")
    time.sleep(delay)
    exit()

time.sleep(delay)
print(colorama.Fore.RED + 'Environmental storytelling with tips on the subject type' + colorama.Style.RESET_ALL)
print('The ghost seems to be invisible. You can only hear its voice.')
print('Throw salt on the floor or punch the air? (salt/punch)')
action = input()
if action == 'salt':
    print('\nYou throw salt on the floor.')
    salt = True
else:
    print('\nYou punch the air.')
    print(colorama.Fore.RED + 'YOURE DEAD' + colorama.Style.RESET_ALL)
    exit()
    salt = False

time.sleep(delay)
if salt:
    print('\nThe ghost becomes visible and starts to talk.')
    print('I am the ghost of the old librarian. I have a riddle for you.')
    print('What is the answer to the ultimate question of life, the universe, and everything?')
    answer = input()
    if answer == '42':
        print('You have answered correctly. I will now let you go.')
    else:
        print('That is not the correct answer. I will not help you.')
        print(colorama.Fore.RED + 'YOURE DEAD' + colorama.Style.RESET_ALL)
        time.sleep(delay)
        exit()
else:
    print('The ghost disappears and you are left alone in the dark.')
    print('You hear a voice saying: "You should have thrown the salt."')
