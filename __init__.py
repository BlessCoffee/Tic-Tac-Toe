from Player import Player
from game_area import game_area
from main_menu import title_screen, selection_menu



area = [["#", "#", "#"], 
        ["#", "#", "#"], 
        ["#", "#", "#"]]


player_1 = Player("Player 1", "X")
player_2 = Player("Player 2", "O")

win = player_1.check_win(area)

print(win)

game_area(area)

title_screen()
selection_menu()