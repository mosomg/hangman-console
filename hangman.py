import sys

if len(sys.argv) > 1:
    secret_word = sys.argv[1].lower()
else:
    secret_word = input("Enter the word to guess: ").lower()

hidden_word = ["_" for _ in secret_word]
print(" ".join(hidden_word))

guess = input("Guess a letter: ").lower()

for index in range(len(secret_word)):
    if secret_word[index] == guess:
        hidden_word[index] = guess

print(" ".join(hidden_word))
