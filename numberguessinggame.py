import random

print("Number guessing game") 
print("Guess a number between 1 and 9")


#letting computer generate a random number from 1 to 9
guess2 = random.randint(1,9)

chance = 0

while chance < 5:
    guess1 = int(input("Enter your guess: "))
    if(guess1 == guess2):
        print("Congratulations You won")
    elif(guess1 < guess2):
        print("Your guess was too low: Guess a number higher than ",guess1)
    else :
        print("Your guess was too high: Guess a number less than ",guess1)
    chance+=1

if not chance < 5 :
    print("You lost")