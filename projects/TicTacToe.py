class Board:

    def __init__(self):
        self.board=[[0]*3 for i in range(3)]

    def display(self): # display the board
        print("\nBoard:")
        for i in range(3):
            for j in range(3):
                print(self.board[i][j],end=" ") 
            print()
        print()

    def placePiece(self,xPos,yPos,piece): #place piece in the board
        if self.board[xPos][yPos]==0:
            self.board[xPos][yPos]=piece
        else:
            raise Exception("Already Used!")

    def checkForWinner(self): #check for the winner
            board=self.board
            
            #row check
            for i in range(3):
                if board[i][0]==board[i][1]==board[i][2]:
                    return board[i][0]

            #column check
            for j in range(3):
                if board[0][j]==board[1][j]==board[2][j]:
                    return board[0][j]
            
            #check cross top-left-start to bottom-right-end
            if board[0][0]==board[1][1]==board[2][2]:
                return board[0][0]

            #check cross top-right-end to bottom-left-start
            if board[0][2]==board[1][1]==board[2][0]:
                return board[0][2]
        
    def clear_the_board(self):  #reset the board
        self.board=[[0]*3 for i in range(3)]

class Game():

    no_of_rounds=0
    print("\n-----------------------------------Welcome to TicTacToe Game!!!-----------------------------------------------\n")
    
    while no_of_rounds<=0: #to get valid round value
        try:
            no_of_rounds=int(input("Enter the no of Round u want to play?"))
        except:
            print("Enter valid Number!")
    
    board=Board() #creating board
    round=1
    
    while round<=no_of_rounds:  #runs till all the rounds are completed
        print(f"\nGame {round}!!\n")
        board.display()
        print("\nPlayer 1 will be X and player 2 will be O\n")
        turn=1

        while True: #runs will the game is won or ends as draw!
            player_no=(turn-1)%2 #for player no 
            print(f"Player {player_no+1} ,Enter the (x,y) postion to place the piece;\n")
            
            while True: #getting valid postion from players to place the piece
                try:
                    xPos=int(input("Enter x value:"))
                    yPos=int(input("Enter y value:"))
                    if xPos>=0 and xPos<=2 and yPos>=0 and yPos<=2:
                        piece="X" if player_no==0 else "O"
                        board.placePiece(xPos,yPos,piece)
                        turn+=1
                        break
                    else:
                        raise Exception("Invaid Position!")
                except Exception as error:
                    print(error)
            
            if turn>=5: # winner can be found only after 5 game turns
                winner=board.checkForWinner()
                if winner=="X":
                    print("\nPlayer 1 wins!\n")
                    board.display()
                    break
                elif winner=="O":
                    print("\nPlayer 2 wins!\n")
                    board.display()
                    break
            
            if turn==10: # if winner not found at turn 10, game is draw!
                print("\nDraw!\n")
                board.display()
                break
            
            board.display()
        board.clear_the_board() #reset board for next round
        round+=1
    print("\n----------------------------- Thank You for playing :) --------------------------------------------\n")