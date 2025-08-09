import random

class GuessTheWordGame:
    def __init__(self):
        self.words = ["characterstics", "wizard", "football", "wuthering", "pneumonoultramicroscopicsilicovolcanoconiosis"]
        self.word = random.choice(self.words)
        self.blank = ["_"] * len(self.word)
        self.lives = 5
        self.already_guessed = set()
    
    def start_game(self):
     print("Welcome to Word Guessinfg Game!")
     print("_".join(self.blank))

     while self.lives > 0:
      guess = input("Guess a letter :").lower()
    
      if not guess.isalpha() or len(guess) != 1:
       print("Invalid entry! Enter a valid input!")
       continue
    
      if guess in self.already_guessed:
        print("You have already guessed that letter. Choose a different letter")
        continue
    
      self.already_guessed.add(guess)
    
      if guess in self.word:
        print("Good! You guessed one!")
        for i in range(len(self.word)):
           if self.word [i] == guess:
               self.blank[i] = guess
        print("_".join(self.blank))
      else: 
        self.lives -= 1 
        print("Wrong guess! Lives left:",(self.lives))
        print("_".join(self.blank))
        
      if "_" not in self.blank:
        print("You win! The word was:", self.word)
        break
     if "_" in self.blank:
      print("Game Over! The word is:", self.word)

game = GuessTheWordGame()
game.start_game()
    
    
