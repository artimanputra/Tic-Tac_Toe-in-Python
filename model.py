global board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = "X"
player_name = "X"
p1 = "X"
p2 = "O"

'''
Print the board in a visually plaesing way
 '''

def printBoard(board):
    for line in board:
        print(line)
    print()


'''
Take user input and replace the appropriate space
'''


def makeMove():
    global player , player_name ,  p1, p2
    print("Player : "+ player_name)
    x = int(input("What is the X Coordinate? "))
    y = int(input("What is the Y Coordinate? "))
    length = len(board)

    ## Checks for the limit and the empty space
    while ((x>=length) or y>=length or board[y][x] != " ")  :
      print("You Must Choose An Empty Spot and A Spot In Range")
      print("Player : "+ player_name)
      x = int(input("What is the X Coordinate? "))
      y = int(input("What is the Y Coordinate? "))

    board[y][x] = player
    win = isWin()
    if win:
      return True
    if player == "X":
        player = "O"
        player_name = p2
    else:
        player = "X"
        player_name = p1
    return False

'''
Did the player win
'''

def isWin():
  global player
  length = len(board)
  ## To check for row completion
  for x in range(length):
    win = True
    for y in range(length):
      if board[x][y] != player:
        win = False
        break
    if win :
      return True
  
  ## To check for column completition
  for x in range(length):
    win = True
    for y in range(length):
      if board[y][x] != player:
        win = False
        break
    if win :
      return True
  
  ## To check for diagonal completion
  win = True
  for c in range(length):
    if board[c][c]!= player:
      win = False
      break
  if win == True:
    return True
  for c in range(length):
    if board[length-1-c][c]!= player:
      win = False
      break
  if win == True :
    return True
  return False

'''
Is the board full
'''
def full():
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j]==" " : 
        return True
  return False

def tictac():
    global player
    if full() : 
      winner = makeMove()
      printBoard(board)
      return winner
    player = "Draw"
    return True


def main():
  global p1,p2,player_name
  print("Welcome To Tic Tac Toe Game")
  p1 = input("Enter Player 1 Name :")
  p2 = input("Enter Player 2 Name :")
  player_name = p1
  gameWon = False
  printBoard(board)
  while gameWon == False :
    gameWon = tictac()
  if player != "Draw":
    print("Congratulations !! " + player_name + " Won")
  else :
    print ("It's A Draw")
  print("GAME OVER !!\nThanks For Joining In")

main()
