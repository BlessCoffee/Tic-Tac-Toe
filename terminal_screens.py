
import time, os
from blessed import Terminal

MENU_OPTIONS = [" New Game ", " Load Game ", " Multiplayer ", "Quit" ] # list of options for main menu

term = Terminal()

def title():
    
    print(term.bold_cyan(term.center("__________________________________________________________________________________________")))
    print(term.bold_cyan(term.center("  _______ __                  _______                          ________                   ")))
    print(term.bold_cyan(term.center(" |       \  \                |       \                        |        \                  ")))
    print(term.bold_cyan(term.center("   \▓▓▓▓▓▓▓▓\▓▓ _______        \▓▓▓▓▓▓▓▓ ______   _______        \▓▓▓▓▓▓▓▓ ______   ______   ")))
    print(term.bold_cyan(term.center("    | ▓▓  |  \/       \______   | ▓▓   |      \ /       \______   | ▓▓   /      \ /      \  ")))
    print(term.bold_cyan(term.center("   | ▓▓  | ▓▓  ▓▓▓▓▓▓▓      \  | ▓▓    \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓      \  | ▓▓  |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\\")))
    print(term.bold_cyan(term.center("    | ▓▓  | ▓▓ ▓▓      \▓▓▓▓▓▓  | ▓▓   /      ▓▓ ▓▓      \▓▓▓▓▓▓  | ▓▓  | ▓▓  | ▓▓ ▓▓    ▓▓ ")))
    print(term.bold_cyan(term.center("    | ▓▓  | ▓▓ ▓▓_____          | ▓▓  |  ▓▓▓▓▓▓▓ ▓▓_____          | ▓▓  | ▓▓__/ ▓▓ ▓▓▓▓▓▓▓▓ ")))
    print(term.bold_cyan(term.center("   | ▓▓  | ▓▓\▓▓     \         | ▓▓   \▓▓    ▓▓\▓▓     \         | ▓▓   \▓▓    ▓▓\▓▓     \\")))
    print(term.bold_cyan(term.center("                     \▓▓   \▓▓ \▓▓▓▓▓▓▓          \▓▓    \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓          \▓▓    \▓▓▓▓▓▓  \▓▓▓▓▓▓▓  by BlessCoffee ")))  
    print(term.bold_cyan(term.center(" __________________________________________________________________________________________")))
    
    # Art by ASCII Generator by https://texteditor.com/multiline-text-art/
    
def menu_options(option = 0):
    
    print("\n")
    print(term.bold_orange(term.center("__________________________________________________________________________________________")))
    print("\n")
    
    if option == 0:
        print(term.center(term.bold_orange_reverse(MENU_OPTIONS[0])))
        position = 5 #
    else:
        print(term.center(term.bold_orange(MENU_OPTIONS[0])))
        
    if option == 1:
        print(term.center(term.bold_orange_reverse(MENU_OPTIONS[1])))
        position = 6 #
    else:
        print(term.center(term.bold_orange(MENU_OPTIONS[1])))

    if option == 2:
        print(term.center(term.bold_orange_reverse(MENU_OPTIONS[2])))
        position = 7 #
    else:
        print(term.center(term.bold_orange(MENU_OPTIONS[2])))
    
    if option == 3:
        print(term.center(term.bold_orange_reverse(MENU_OPTIONS[3])))
        position = 8 #
    else:
        print(term.center(term.bold_orange(MENU_OPTIONS[3])))

    print(term.bold_orange(term.center("__________________________________________________________________________________________")))
    
    return position # returns cursor position of the option in the menu
    
def option_blink(position):
    #bugged needs fixing
    print(term.move_up(position), end='')
    print(term.center(term.bold_orange(MENU_OPTIONS[0])))
    print(term.move_down(position), end='')

    time.sleep(0.6)

    print(term.move_up(position), end='')
    print(term.center(term.bold_orange_reverse(MENU_OPTIONS[0])))
    print(term.move_down(position), end='')

def menu_main():
    with term.cbreak(), term.hidden_cursor():
        print(term.home + term.clear_eos)
        title()
        option = menu_options()
        while True:
            key = term.inkey(timeout=0.6)
            if key.name == "KEY_UP":
                option = (option - 1) % len(MENU_OPTIONS)
                print(term.home + term.clear_eos)
                title()
                menu_options(option)
            elif key.name == "KEY_DOWN":
                option = (option + 1) % len(MENU_OPTIONS)
                print(term.home + term.clear_eos)
                title()
                menu_options(option)
            elif key.name == "KEY_ENTER" or key == "\n":
                # if option == MENU_OPTIONS.index(" Quit "):
                # os.system('cls' if os.name == 'nt' else 'clear')
                # return
                return option
            elif key == 'q':
                os.system('cls' if os.name == 'nt' else 'clear')
                return len(MENU_OPTIONS) - 1  # Return the index for "Quit" option
                
            