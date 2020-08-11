Board=[1,2,3,4,5,6,7,8,9]    
pieceToMove='X'
def DisplayBoard():

        print("\n----------")

        print("|",Board[0],"|",Board[1],"|",Board[2],"|")
        print("|",Board[3],"|",Board[4],"|",Board[5],"|")
        print("|",Board[6],"|",Board[7],"|",Board[8],"|")
        
        print("\n----------")
def makemove():

        print("Press the number of the field :")
        position=int(input())
        
        if ((Board[position-1]=='X') or (Board[position-1]=='O')):
            print("Player ",pieceToMove," choose already occupied field you lose your turn")

        else:
             Board[position-1]=pieceToMove


        

def checkBoard():

        #//first player
        if (Board[0]=='X' and Board[1]=='X' and Board[2]=='X'):
            
            return 'X'
        
        if (Board[3]=='X' and Board[4]=='X' and Board[5]=='X'):
        
            
            return 'X';

        if (Board[6]=='X' and Board[7]=='X' and Board[8]=='X'):
            return 'X'
        
        if (Board[0]=='X' and Board[3]=='X' and Board[6]=='X'):
        
            
            return 'X';
        if (Board[1]=='X' and Board[4]=='X' and Board[7]=='X'):
            
            return 'X'
        
        if (Board[2]=='X' and Board[5]=='X' and Board[8]=='X'):
        
            
            return 'X';
        if (Board[0]=='X' and Board[4]=='X' and Board[8]=='X'):
            
            return 'X'
        
        if (Board[2]=='X' and Board[4]=='X' and Board[6]=='X'):
        
            win=1;
            return 'X';
        #player2
        if (Board[0]=='O' and Board[1]=='O' and Board[2]=='O'):
            
            return 'O'
        
        if (Board[3]=='O' and Board[4]=='O' and Board[5]=='O'):
        
            
            return 'O';

        if (Board[6]=='O' and Board[7]=='O' and Board[8]=='O'):
            
            return 'O'
        
        if (Board[0]=='O' and Board[3]=='O' and Board[6]=='O'):
        
            
            return 'O';
        if (Board[1]=='O' and Board[4]=='O' and Board[7]=='O'):
            return 'O'
        
        if (Board[2]=='O' and Board[5]=='O' and Board[8]=='O'):
            return 'O';
        if (Board[0]=='O' and Board[4]=='O' and Board[8]=='O'):
            return 'O'
        
        if (Board[2]=='O' and Board[4]=='O' and Board[6]=='O'):
        
            
            return 'O';
        return '/';

#main

print("Welcome to the TicTacToe game!\nTake turns entering the position (1..9)\ninto which your piece will be placed.\nPress any number to start\nenter '0' for exit");
k=int(input())
if k==0:
    exit()

else:
    DisplayBoard();
    while (1):
        makemove()

        DisplayBoard()

        if (checkBoard() == 'X'):
            print( "X wins!" );
            break;
            
        elif (checkBoard() == 'O'):
            print( "O wins!" );
            break;
        if pieceToMove=='X':
            pieceToMove='O'
        else:
            pieceToMove='X'


 

    

