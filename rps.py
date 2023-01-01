'''
##    ###        #       ##
#  #  #----       # #     #  #
##    #         # # #   #  #
#  #  ###  #       #  ##
Hello!
Made by SohalSaab36 
COPYRIGHT
Original Source : GitHub
Happy Weekend
current version v 5.1
##    ##   ###
#  # # #  #----
#   #   #  #
#        #  ###
'''
import random

def play_game():
  # list of possible moves
  moves = ['rock', 'paper', 'scissors']

  # get player's move
  player_move = input(f"{moves}:").lower()
  if player_move not in moves:
    print("Invalid move. Please enter rock, paper, or scissors.")
    return

  # get computer's move
  computer_move = random.choice(moves)
  print(f"player choice {player_move} and computer choice {computer_move}")  
    
  # determine the winner
  if player_move == computer_move:
    print("It's a tie!")
  elif (player_move == 'rock' and computer_move == 'scissors') or \
       (player_move == 'paper' and computer_move == 'rock') or \
       (player_move == 'scissors' and computer_move == 'paper'):
    print("You win!")
    return 1 # return 1 point for player
  else:
    print("Computer wins!")
    return -1 # return -1 point for computer

# initialize scores
player_score = 0
computer_score = 0

# play the game multiple times
while True:
  result = play_game()
  if result == 1:
    player_score += 1
  elif result == -1:
    computer_score += 1
  else:
    pass

  # print scores
  print(f"Player: {player_score} | Computer: {computer_score}")

  # ask if player wants to continue
  continue_playing = input("Do you want to play again? (y/n) ").lower()
  if continue_playing == 'y':
    pass
  elif continue_playing == "n":
      break
  else:
      pass

print("Thanks for playing!")
