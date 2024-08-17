import random 

number = random.randint(0,100) 
guess = 0

while guess != number:
    
    guess = int(input("Enter Guess:"))
    
    if guess > number:
        print("Your Guess is Higher")
    elif guess < number:
        print("Your Guess is Lower")
    else:
        print("You Won")
