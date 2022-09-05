import random, os

os.system("cls")

print("-"*50, "MAGIC NUMBER GAME", "-"*50)
magic_number = random.randint(1, 10)
player_guess = input("What is my number?")

while player_guess != str(magic_number):
    print("Wrong :( Try again!")
    player_guess = input("What is my number?")

print(f"You guessed it!! It was {magic_number}")