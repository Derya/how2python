"""
Baseline example of a REPL. Our program has two commands that the user
can enter that make the program do stuff, and they can also quit the
program.
"""

# describe available commands
print("== COMMANDS ==")
print("hello -> say hello")
print("sing -> sing a song")
print("quit -> exit the program")

# define a boolean that can be used to end our read-eval-print-loop
shouldContinue = True

# loop forever, until we shouldn't anymore
while shouldContinue:
  # read the next command
  user_command = input("Enter your command:\n")

  if user_command == "hello":
    # say hello
    print("Hello!")
  elif user_command == "sing":
    # sing a song
    print("Yo listen up, here's the story / About a little guy that / lives in a blue world / And all day and all "
          "night and everything he sees is just blue...")
  elif user_command == "quit":
    # set the shouldContinue boolean to false so that our loop exits
    print("Okay, goodbye!")
    shouldContinue = False
  else:
    # command is unknown, do nothing other than alerting the user as such
    print(f"Unknown command '{user_command}'!")
