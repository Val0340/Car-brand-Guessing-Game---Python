import random

answer= input("Hello, Welcome to the car brand guessing game. Would you like to play?: ")

if answer == "no":
    exit()
elif answer == "yes":
    print("Great ! Let's play!")
else:
    print("Error : choose yes or no")
    exit()
    
words = [ "porshe" , "toyota", "honda", "hyundai", "ferrari", "infiniti", "ford", "volvo", "lamborghini","dodge"]

word = random.choice(words)


print("Guess the characters")


guesses = ""

turns = 10



while turns > 0 :
    wrong = 0
    
    for letter in word:
        
        if letter in guesses:
            print(letter, end=" ")
        else:
            print ( "_")
        
            wrong +=1
        
    if wrong == 0:
        print("You win")
    
        print("The word is : ", word)
        break

    print()
    guess= input("Guess one letter of the car brand: ")
    guesses += guess

    if guess not in word :
        turns -= 1
    
        print("Try again")
    
        print("You have", + turns, "more guesses")
        if turns == 0 :
            print("You lose")
    