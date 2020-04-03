import random 

class Player:
    def __init__(self, player_name, player_token): #Creates class that defines the input for user name and choice of token.
        self.player_name = player_name
        self.player_token = player_token
    
    def name(self):  #Defines user input of name.
        name = input('Please enter your name: ')
        return name
    
    def token(self): #Defines user choice of X or O
        token = input('Would you like X\'s or O\'s? : ')
        if token.lower == 'o':
            return 'O'
        else:
            token.lower == 'x':
            return 'X'


class Game:

    def __init__(self, board):
        self.board = ['0,0', '1,0', '2,0', '0,1', '1,1', '2,1', '0,2', '1,2', '2,2'] 
   
    def __repr__(self): #Returns a pretty string representation of the game board
        board = [ 
                 [" ","|"," ",'|'," "],
                 ["-","-","-","-","-"],
                 [" ","|"," ","|"," "],
                 ["-","-","-","-","-"],
                 [" ","|"," ","|"," "]
                ]
#
"""
if we want "x" in the middle: 

user_input = "x"
user_positon = ?,?
in_play_board[2][2] = user_position

reprint the board with the replacement. in_play_board = board

# for i in board:
#     print(i[0], i[1], i[2])
    
    def move(self, position, player): #Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
        player_input = input('Please enter the position to place your piece (1-9): ')
                
        coordinates = {
                        "1" : "0,0",
                        "2" : "0,1",
                        "3" : "0,2", 
                        "4" : "1,0",
                        "5" : "1,1", 
                        "6" : "1,2",
                        "7" : "2,0",
                        "8" : "2,1",
                        "9" : "2,2"
                       }
                
        position = coordinates[player_input]
        
        return position
        
    def calc_winner(self): #What token character string has won or None if no one has.
        if #something is in (123, 456, 789, 147, 258, 369, 159, 357):
            #then winning result
        else:
            #continue playing
        ((0,0) (0,1) (0,2))
        ((0,0) (1,0) (2,0)) 
        ((0,0) (1,1) (2,2))
        ((1,0) (1,1) (1,2))  
        ((0,1) (1,1) (2,1))
        ((0,2) (1,2) (2,2))
        ((2,0) (2,1) (2,2))
    
    
    def is_full(self): #Returns true if the game board is full.
    
    def is_game_over(self): #Returns true if the game board is full or a player has won.




    


def main():

    while True:
        play = input('Would you like to play a game of Tic-tac-toe?\n Type: yes OR no')
        if play == 'yes':
            continue
        elif play == 'no':
            break
            
    player1_name = Player.name(self)
    player1_token = Player.token(self)
    player1 = Player(player1_name, player1_token)

    player2_name = Player.name(self)
    player2_token = Player.token(self)
    player2 = Player(player2_name, player2_token)
    

    
    #main function to start the game
    # def play_game():
    #      board, winner,counter = creat_board (), 0,1
    #      print(board)
    #      sleep(2)  # the sleep(2) suspends the fuction a given amount of seconds

    #     while winner == 0:
    #         for player in [1,2]:
    #             board = random_place(board,playe)  #come back to this(because there is a player1_name and player2_name)
    #             print('board after'+ str(counter) + "move")
    #             print(board)
    #             sleep(2) 
    #             counter += 1
    #             winner = evaluate(board)
    #             if winner != 0:
    #                 break
    #     return(winner)
    
    



    