import random

number = random.randint(1, 10)
guess = 0

while guess != number:
    guess = int(input("Enter a number: "))
    
    if guess < number:
        print("Too small")
    elif guess > number:
        print("Too big")
    else:
        print("Congratulations! You found the number")
        
        