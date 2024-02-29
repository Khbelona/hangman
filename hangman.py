

import random
import hangman_words


chosen_word=random.choice(hangman_words.word_list)
lives=6
from hangman_art import logo
print(logo)
print(f"The random chosen word is {chosen_word}")
display=[]

for _ in range(len(chosen_word)):
    display+="_"
print(display)
end_of_game=False

while not end_of_game:
    guess=input("Guess your letter").lower()
    if guess in display:
        print(f"you have already gueess ,this letter {guess}")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"you guessed {guess}, this is not in the word . So you lose a life")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose this game")
      
    print(f"{''.join(display)}")
    
    if "_" not in display:
        end_of_game=True
        print("YOU WIM THIS GAME!!!")
    from hangman_art import stages

    print(stages[lives])

