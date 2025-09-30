import random

def get_player_choice(): 
  return input("Enter your choice (rock, paper, or scissors) ")

def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)

def determine_winner(player, computer):
  if (player == "rock" and computer == "scissors") or \
     (player == "scissors" and computer == "paper") or \
     (player == "paper" and computer == "rock"):
    return "player"
  elif player == computer:
    return "tie"
  else:
    return "computer"

def play_game():
  player_wins = 0
  computer_wins = 0

  while player_wins < 2 and computer_wins < 2:
    player_choice = get_player_choice().lower()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner(player_choice, computer_choice)
    
    if winner == "player": 
      print("You won this round!")
      player_wins += 1 
    elif winner == "computer": 
      print("The Computer won this round.")
      computer_wins += 1 
    else: 
      print("It's a tie") 

    print(f"Current Score - Player: {player_wins}, Computer {computer_wins}")

    if player_wins == 2: 
      print("Congratulations! You won the best of 3 series!")
    elif computer_wins == 2:
      print("The Computer won the best of 3 series.")
    else: 
      continue 
 
play_game()