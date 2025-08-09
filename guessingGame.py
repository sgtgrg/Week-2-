import random

words = ["characterstics", "wizard", "football", "wuthering", "pneumonoultramicroscopicsilicovolcanoconiosis"]

word = random.choice(words)

blank = ["_"] * len(word)

lives = 5

print("Welcome to Word Guessinfg Game!")
print("_".join(blank))

while lives > 0:
    guess = input("Guess a letter :")
    
    if guess in word:
        for i in range(len(word)):
           if word [i] == guess:
               blank[i] = guess
    else: 
        lives -= 1 
        print("Wrong guess! Lives left:",(lives))
        
    print("_".join(blank))
    
    if "_" not in blank:
        print("You win! The word was:", word)
        break

if "_" in blank:
    print("Game Over! The word is:", word)
