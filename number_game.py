secret = 6
guess = int(input("Guess a number between 1 and 10!: "))
if guess == secret:
  print("Correct!")
elif guess >= secret:
  print("Too big")
elif guess <= secret:
  print("Too small")  
