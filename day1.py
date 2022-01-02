# guessing game

import random
print("Hi there, what's your name?")
userName = input()
print("Well, " + userName + " guess a number between one and ten. If you guess right, you win")
secretNumber = random.randint(1, 10)
for _ in range(4):
    print("Take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("Too low!")
    elif guess > secretNumber:
        print("Too high!")
    else:
        print("Good job!")
        break
else:
    print("Good try! The number I was thinking of was " + str(secretNumber))
