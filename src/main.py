# TIC-TAC-TOE by @WhaleWellWell on GitHub

X = "x"
O = "O"
LEGAL_MOVES = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
SPACE = "."
BOARD_TOP    = [ "{}".format(SPACE), "{}".format(SPACE), "{}".format(SPACE) ]
BOARD_MIDDLE = [ "{}".format(SPACE), "{}".format(SPACE), "{}".format(SPACE) ]
BOARD_BOTTOM = [ "{}".format(SPACE), "{}".format(SPACE), "{}".format(SPACE) ]

def displayBoard():
  print("\n")
  print("  ABC")
  print("1 " + BOARD_TOP[0] + BOARD_TOP[1] + BOARD_TOP[2])
  print("2 " + BOARD_MIDDLE[0] + BOARD_MIDDLE[1] + BOARD_MIDDLE[2])
  print("3 " + BOARD_BOTTOM[0] + BOARD_BOTTOM[1] + BOARD_BOTTOM[2])
  print("\n")

def askForMove(player):
  while True:
    print("Please enter move, player " + player + "")
    move = input("> ").capitalize()

    if move in LEGAL_MOVES:

      # A
      if move == "A1":
        if BOARD_TOP[0] == SPACE:
          BOARD_TOP[0] = player
        else:
          print("Not a legal move :{\n")
          continue

      if move == "A2":
        if BOARD_MIDDLE[0] == SPACE:
          BOARD_MIDDLE[0] = player
        else:
          print("Not a legal move :{\n")
          continue

      if move == "A3":
        if BOARD_BOTTOM[0] == SPACE:
          BOARD_BOTTOM[0] = player
        else:
          print("Not a legal move :{\n")
          continue

      # B
      if move == "B1":
        if BOARD_TOP[1] == SPACE:
          BOARD_TOP[1] = player
        else:
          print("Not a legal move :{\n")
          continue

      if move == "B2":
        if BOARD_MIDDLE[1] == SPACE:
          BOARD_MIDDLE[1] = player
        else:
          print("Not a legal move :{\n")
          continue

      if move == "B3":
        if BOARD_BOTTOM[1] == SPACE:
          BOARD_BOTTOM[1] = player
        else:
          print("Not a legal move :{\n")
          continue

      # C
      if move == "C1":
        if BOARD_TOP[2] == SPACE:
          BOARD_TOP[2] = player
        else:
          print("Not a legal move :{\n")
          continue

      if move == "C2":
        if BOARD_MIDDLE[2] == SPACE:
          BOARD_MIDDLE[2] = player
        else:
          print("Not a legal move :{\n")
          continue

      if move == "C3":
        if BOARD_BOTTOM[2] == SPACE:
          BOARD_BOTTOM[2] = player
        else:
          print("Not a legal move :{\n")
          continue

      break

    else:
      print("Not a legal move :{\n")
      continue

# Main Loop:
def main():
  turn = O
  print("Welcome to TIC-TAC-TOE")
  while True:
    if turn == X:
      turn = O
    else:
      turn = X

    displayBoard()
    askForMove(turn)

    if BOARD_TOP[0] == turn and BOARD_TOP[1] == turn and BOARD_TOP[2] == turn:
      victory()
      break
    if BOARD_MIDDLE[0] == turn and BOARD_MIDDLE[1] == turn and BOARD_MIDDLE[2] == turn:
      victory()
      break
    if BOARD_BOTTOM[0] == turn and BOARD_BOTTOM[1] == turn and BOARD_BOTTOM[2] == turn:
      victory()
      break
    if BOARD_TOP[0] == turn and BOARD_MIDDLE[1] == turn and BOARD_BOTTOM[2] == turn:
      victory()
      break
    if BOARD_TOP[2] == turn and BOARD_MIDDLE[1] == turn and BOARD_BOTTOM[0] == turn:
      victory()
      break
    if BOARD_TOP[0] == turn and BOARD_MIDDLE[0] == turn and BOARD_BOTTOM[0] == turn:
      victory()
      break
    if BOARD_TOP[1] == turn and BOARD_MIDDLE[1] == turn and BOARD_BOTTOM[1] == turn:
      victory()
      break
    if BOARD_TOP[2] == turn and BOARD_MIDDLE[2] == turn and BOARD_BOTTOM[2] == turn:
      victory()
      break

    if BOARD_TOP[0] != "." and BOARD_TOP[1] != "." and BOARD_TOP[2] != "." and BOARD_MIDDLE[0] != "." and BOARD_MIDDLE[1] != "." and BOARD_MIDDLE[2] != "." and BOARD_BOTTOM[0] != "." and BOARD_BOTTOM[1] != "." and BOARD_BOTTOM[2] != ".":
      displayBoard()
      print("\n\nCAT got it! Play Again?")
      print("""       _                        
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-
       .       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
      .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'
      """)
      playAgain = input("Play Again? (y) (n)\n> ").capitalize()
      if playAgain == "Y":
        main()
      else: 
        break

def victory():
  displayBoard()
  print("\n\nVictory!! Great Job!")
  print("""                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
        *
        *""")
  playAgain = input("Play Again? (y) (n)\n> ").capitalize()
  if playAgain == "Y":
    main()
  else:
    pass


if __name__ == '__main__':
  main()
