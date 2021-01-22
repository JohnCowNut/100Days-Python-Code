import random
# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
idx_random = random.randint(0, 2)
chosen_word = word_list[idx_random]
print('Choose word' + chosen_word)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter: ').lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in range(0, len(chosen_word)):
    if chosen_word[i] == guess:
        print('Right !')
    else:
        print('Wrong !')
