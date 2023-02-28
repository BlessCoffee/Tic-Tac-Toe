
from blessed import Terminal




def main_menu():
  
    term = Terminal()
    
    menu_options = ["New Game", "Load Game", "Multiplayer", "Quit" ]
    
    print(term.bold_cyan(term.center("__________________________________________________________________________________________")))
    print(term.bold_cyan(term.center("_________ __                 ________                         _________                   ")))
    print(term.bold_cyan(term.center("|        \  \               |        \                        |        \                  ")))
    print(term.bold_cyan(term.center("\ ▓▓▓▓▓▓▓▓\▓▓_______        \▓▓▓▓▓▓▓▓ ______   _______        \▓▓▓▓▓▓▓▓ ______   ______   ")))
    print(term.bold_cyan(term.center(" | ▓▓  |  \/       \______   | ▓▓   |      \ /       \______   | ▓▓   /      \ /      \  ")))
    print(term.bold_cyan(term.center(" | ▓▓  | ▓▓  ▓▓▓▓▓▓▓      \  | ▓▓    \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓      \  | ▓▓  |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\\")))
    print(term.bold_cyan(term.center("  | ▓▓  | ▓▓ ▓▓      \▓▓▓▓▓▓  | ▓▓   /      ▓▓ ▓▓      \▓▓▓▓▓▓  | ▓▓  | ▓▓  | ▓▓ ▓▓    ▓▓ ")))
    print(term.bold_cyan(term.center("  | ▓▓  | ▓▓ ▓▓_____          | ▓▓  |  ▓▓▓▓▓▓▓ ▓▓_____          | ▓▓  | ▓▓__/ ▓▓ ▓▓▓▓▓▓▓▓ ")))
    print(term.bold_cyan(term.center(" | ▓▓  | ▓▓\▓▓     \         | ▓▓   \▓▓    ▓▓\▓▓     \         | ▓▓   \▓▓    ▓▓\▓▓     \\")))
    print(term.bold_cyan(term.center("                  \▓▓   \▓▓ \▓▓▓▓▓▓▓          \▓▓    \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓          \▓▓    \▓▓▓▓▓▓  \▓▓▓▓▓▓▓  by BlessCoffee ")))  
    print(term.bold_cyan(term.center(" __________________________________________________________________________________________")))
    
    # Art bu ASCII Generator by https://texteditor.com/multiline-text-art/
    
    print("/n")
    print(term.bold_orange(term.center("__________________________________________________________________________________________")))
    print("/n")
    print(term.bold_orange(term.center(menu_options[0])))
    print(term.bold_orange(term.center(menu_options[1])))
    print(term.bold_orange(term.center(menu_options[2])))
    print(term.bold_orange(term.center(menu_options[3])))
    print(term.bold_orange(term.center("__________________________________________________________________________________________")))
    print("\n")


