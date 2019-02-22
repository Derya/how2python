"""
Example of using a REPL to implement an extremely DEEP and MEANINGFUL
turn based game against an advanced AI.

Let's imagine a dumb game where the player can choose to either win or
lose each round. If the player or the AI win 3 rounds, the game ends.
"""

import sys

# describe the commands for playing this game
print("== COMMANDS ==")
print("win -> win a round")
print("forfeit -> concede a round")
print("quit -> exit the program")
print()

# describe the game's rules
print("First player to win three rounds wins.")
print()

# start scores at 0
user_score = 0
opponent_score = 0


# define a helper function for printing the current scores
def print_scores():
  print(f"You have won {user_score} rounds, and your opponent has won {opponent_score} rounds.")


# while both scores are less than 3, the game is not over yet
while user_score < 3 and opponent_score < 3:
  # read the next command
  user_command = input("Enter your command:\n")

  if user_command == "win":
    # increment user score by 1 and print both scores
    user_score += 1
    print_scores()
  elif user_command == "forfeit":
    # increment opponent score by 1 and print both scores
    opponent_score += 1
    print_scores()
  elif user_command == "quit":
    # quit the program
    print("Okay, goodbye!")
    sys.exit()
  else:
    # command is unknown, do nothing other than alerting the user as such
    print(f"Unknown command '{user_command}'!")

# print the outcome of the game
if user_score >= 3:
  print("You have won the game!")
else:
  print("You have lost the game!")
