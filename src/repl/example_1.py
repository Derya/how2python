"""
Baseline example of reading and writing to the CLI.

This program only reads from the console once, and does what
you tell it to and then exits. Not very useful, typically we'd
just use flags for this instead of prompting the user for an
input.
"""

# describe available commands
print("== COMMANDS ==")
print("hello -> say hello")
print("sing -> sing a song")

# read the user's command
user_command = input('Enter your command:\n')

if user_command == "hello":
  # say hello
  print("Hello!")
elif user_command == "sing":
  # sing a song
  print("Yo listen up, here's the story / About a little guy that / lives in a blue world / And all day and all night "
        "and everything he sees is just blue...")
else:
  # command is unknown, do nothing other than alerting the user as such
  print(f"Unknown command '{user_command}'!")
