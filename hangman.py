import sys

if len(sys.argv) > 1:
    secret_word = sys.argv[1]
else:
    secret_word = input("Enter the word to guess: ")

hidden_word = ["_" for _ in secret_word]
print(" ".join(hidden_word))

guess = input("Guess a letter: ")

for index in range(len(secret_word)):
    if secret_word[index].lower() == guess.lower():
        hidden_word[index] = secret_word[index]

print(" ".join(hidden_word))
