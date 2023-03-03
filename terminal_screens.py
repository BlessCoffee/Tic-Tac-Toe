
import time
from blessed import Terminal


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
    
    # Art bu ASCII Generator by https://texteditor.com/multiline-text-art/
    
def menu_options(option = 0):
    
    menu_options = [" New Game ", " Load Game ", " Multiplayer ", " Quit " ]
    
    print("\n")
    print(term.bold_orange(term.center("__________________________________________________________________________________________")))
    print("\n")
    
    if option == 0:
        print(term.center(term.bold_orange_reverse(menu_options[0])))
    else:
        print(term.center(term.bold_orange(menu_options[0])))
        
    if option == 1:
        print(term.center(term.bold_orange_reverse(menu_options[1])))
    else:
        print(term.center(term.bold_orange(menu_options[1])))

    if option == 2:
        print(term.center(term.bold_orange_reverse(menu_options[2])))
    else:
        print(term.center(term.bold_orange(menu_options[2])))
    
    if option == 3:
        print(term.center(term.bold_orange_reverse(menu_options[3])))
    else:
        print(term.center(term.bold_orange(menu_options[3])))

    
    print(term.bold_orange(term.center("__________________________________________________________________________________________")))
    print("\n")

def menu_main():
    
    title()
    menu_options()
    #while True:
    print(term.move_up(7) + "")
    
    print(term.move_down(7))
    

        
    #time.sleep(0.8)
    #print(term.clear())
