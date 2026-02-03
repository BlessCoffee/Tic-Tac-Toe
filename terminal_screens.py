
import time, os
from blessed import Terminal

MENU_OPTIONS = [" New Game ", " Load Game ", " Multiplayer ", " Quit " ] # list of options for main menu

term = Terminal()

def title():
    
    print(term.bold_cyan(term.center("__________________________________________________________________________________________")))
    print(term.bold_cyan(term.center("  ______  __                  _______                           _______                    ")))
    print(term.bold_cyan(term.center(" |      \ \ \                |       \                         |       \                  ")))
    print(term.bold_cyan(term.center("  \▓▓▓▓▓▓▓▓ ▓▓ _______        \▓▓▓▓▓▓▓▓ ______   _______        \▓▓▓▓▓▓▓▓ ______   ______   ")))
    print(term.bold_cyan(term.center("    | ▓▓  |  \/       \______   | ▓▓   |      \ /       \______   | ▓▓   /      \ /      \  ")))
    print(term.bold_cyan(term.center("   | ▓▓  | ▓▓  ▓▓▓▓▓▓▓      \  | ▓▓    \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓      \  | ▓▓  |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\\")))
    print(term.bold_cyan(term.center("    | ▓▓  | ▓▓ ▓▓      \▓▓▓▓▓▓  | ▓▓   /      ▓▓ ▓▓      \▓▓▓▓▓▓  | ▓▓  | ▓▓  | ▓▓ ▓▓    ▓▓ ")))
    print(term.bold_cyan(term.center("    | ▓▓  | ▓▓ ▓▓_____          | ▓▓  |  ▓▓▓▓▓▓▓ ▓▓_____          | ▓▓  | ▓▓__/ ▓▓ ▓▓▓▓▓▓▓▓ ")))
    print(term.bold_cyan(term.center("   | ▓▓  | ▓▓\▓▓     \         | ▓▓   \▓▓    ▓▓\▓▓     \         | ▓▓   \▓▓    ▓▓\▓▓     \\")))
    print(term.bold_cyan(term.center("                    \▓▓   \▓▓ \▓▓▓▓▓▓▓          \▓▓    \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓          \▓▓    \▓▓▓▓▓▓  \▓▓▓▓▓▓▓  by Ajay Samuel")))  
    print(term.bold_cyan(term.center(" __________________________________________________________________________________________")))
    
    # Art by ASCII Generator by https://texteditor.com/multiline-text-art/
    
def menu_options(option = 0):
    term.move_xy(0,0)
    print(term.bold_orange("\n" + term.center("__________________________________________________________________________________________" + "\n")))
    
    if option == 0:
        print(term.center(term.bold_orange_reverse(MENU_OPTIONS[0])))
    else:
        print(term.center(term.bold_orange(MENU_OPTIONS[0])))
        
    if option == 1:
        print(term.center(term.bold_orange_reverse(MENU_OPTIONS[1])))
    else:
        print(term.center(term.bold_orange(MENU_OPTIONS[1])))

    if option == 2:
        print(term.center(term.bold_orange_reverse(MENU_OPTIONS[2])))
    else:
        print(term.center(term.bold_orange(MENU_OPTIONS[2])))
    
    if option == 3:
        print(term.center(term.bold_orange_reverse(MENU_OPTIONS[3])))
    else:
        print(term.center(term.bold_orange(MENU_OPTIONS[3])))

    print(term.bold_orange(term.center("__________________________________________________________________________________________")))
    
    
def option_blink(option):
    term.move_xy(0,0)
    option_postion_x = option + 15
    print(term.home + term.center(term.move_down(option_postion_x) + term.bold_orange(MENU_OPTIONS[option])))
    time.sleep(0.7)
    print(term.home + term.center(term.move_down(option_postion_x) + term.bold_orange_reverse(MENU_OPTIONS[option])))

def menu_main():
    with term.cbreak(), term.hidden_cursor():
        option = 0
        print(term.home + term.clear_eos)
        title()
        menu_options(option)
        while True:
            option_blink(option)
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
                return os.system('cls' if os.name == 'nt' else 'clear')
            elif key == 'q':
                os.system('cls' if os.name == 'nt' else 'clear')
                return len(MENU_OPTIONS) - 1  # Return the index for "Quit" option
                
            