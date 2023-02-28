from Player import Player
from game_area import game_area
from terminal_screens import main_menu


area = [["#", "#", "#"], 
        ["#", "#", "#"], 
        ["#", "#", "#"]]


player_1 = Player("Player 1", "X")
player_2 = Player("Player 2", "O")

win = player_1.check_win(area)

print(win)

game_area(area)

main_menu()