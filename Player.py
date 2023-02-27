
class Player:
    
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    

    def check_win(self, area):  # Check if the player wins if meets the wining condition
            if area[0][0] == area[0][1] == area[0][2] == self.symbol:
                    return True
            elif area[1][0] == area[1][1] == area[1][2] == self.symbol:
                    return True
            elif area[2][0] == area[2][1] == area[2][2] == self.symbol:
                    return True
            elif area[0][0] == area[1][0] == area[2][0] == self.symbol:
                    return True
            elif area[0][1] == area[1][1] == area[2][1] == self.symbol:
                    return True
            elif area[0][2] == area[1][2] == area[2][2] == self.symbol:
                    return True
            elif area[0][0] == area[1][1] == area[2][2] == self.symbol:
                    return True
            elif area[0][2] == area[1][1] == area[1][2] == self.symbol:
                    return True
            else:
                    return False
    





        

