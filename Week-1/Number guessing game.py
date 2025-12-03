import random
num=random.randint(1,100)
guess = input("Guess a number between 1 and 100: ")
if guess==num:
    print("Correct!",num)
else :
    print("Incorrect! the guess is ",guess," And the number was ",num)
