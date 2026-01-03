import random
import hangman_words
import hangman_art

words = random.choice(hangman_words.word_list)
lives = 6

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
wrong_letters = []

while not game_over:

    print("****************************" + str(lives) + " LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You have already guessed this letter, please try again.")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        wrong_letters.append(guess)
        print("You guessed " + str(guess) + ", that's not in the word. You lose a life.")
        print("You have " + str(lives) + " lives left.")
        print("You have guessed " + str(wrong_letters) + " so far.")
        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print("You were trying to guess " + str(chosen_word))

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
