from pick import pick

def title_screen():
    print("__________________________________________________________________________________________")
    print("""
_________ __                 ________                         _________  
|        \  \               |        \                        |        \                  
\▓▓▓▓▓▓▓▓\▓▓ _______        \▓▓▓▓▓▓▓▓ ______   _______        \▓▓▓▓▓▓▓▓ ______   ______  
  | ▓▓  |  \/       \______   | ▓▓   |      \ /       \______   | ▓▓   /      \ /      \ 
  | ▓▓  | ▓▓  ▓▓▓▓▓▓▓      \  | ▓▓    \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓      \  | ▓▓  |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\\
  | ▓▓  | ▓▓ ▓▓      \▓▓▓▓▓▓  | ▓▓   /      ▓▓ ▓▓      \▓▓▓▓▓▓  | ▓▓  | ▓▓  | ▓▓ ▓▓    ▓▓
  | ▓▓  | ▓▓ ▓▓_____          | ▓▓  |  ▓▓▓▓▓▓▓ ▓▓_____          | ▓▓  | ▓▓__/ ▓▓ ▓▓▓▓▓▓▓▓
  | ▓▓  | ▓▓\▓▓     \         | ▓▓   \▓▓    ▓▓\▓▓     \         | ▓▓   \▓▓    ▓▓\▓▓     \\
    \▓▓   \▓▓ \▓▓▓▓▓▓▓          \▓▓    \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓          \▓▓    \▓▓▓▓▓▓  \▓▓▓▓▓▓▓  by BlessCoffee
          """)
    print("__________________________________________________________________________________________")

    # Art bu ASCII Generator by https://texteditor.com/multiline-text-art/


def selection_menu():
  title = 'Please choose your favorite programming language: '
  options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']

  option, index = pick(options, title, indicator='=>', default_index=2)