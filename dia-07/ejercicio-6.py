import random

from hangman_logo import logo
print(logo)

from hangman_word_list import word_list

from hangman_stages import stages
stages 

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You lose a life")
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])