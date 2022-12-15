

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
] # this is a generic borad with a valid game. empty spaces are shown as 0


def print_board(board):
    """
    This function main goal is to print the board in the terminal
    It is interesting to have a visual representation
    """

    for y in range(len(board)):
        if y%3 == 0 and y != 0: # printing the divisions between the squares 3*3
            print("- - - - - - - - - - - - - - ") 
    
        for x in range(len(board[0])):
            if x%3 == 0 :
                print(" | ", end="") # vertical division on 3*3
            if x==8:
                if board[y][x] !=0:
                    print(str((board[y][x])))
                else:
                    print("  ")
            else:
                if board[y][x] !=0:
                    print(str((board[y][x]))+" ", end="")
                else:
                    print("  ", end="")


def find_empty(board):
    """
    find the empty spaces and return it
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j) # row, column


def valid (board, num, pos):
    """
    See if the number put in a blanck position is valid or not
    """

    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1]!=i: # check elements in row to see if there is a similar number to the one being inserted
            return False
    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0]!=i: # check elements in column to see if there is a similar number to the one being inserted
            return False

    # check the 3*3 square to see if there is already the same number
    # defining the box position
    box_x= pos[1]//3
    box_y= pos[0]//3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j]==num:
                return False