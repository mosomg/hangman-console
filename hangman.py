import sys

STAGES = [
    r"""
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      -----
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """,
]

if len(sys.argv) > 1:
    secret_word = sys.argv[1].strip()
else:
    secret_word = input("Enter the word to guess: ").strip()

if not secret_word or not secret_word.isalpha():
    print("Error: Secret word must contain only letters.")
    sys.exit(1)

hidden_word = ["_" for _ in secret_word]
guessed_letters = []
lives = 6

print(STAGES[6 - lives])
print(" ".join(hidden_word))
print("Guessed letters:", ", ".join(guessed_letters))
print("Lives:", lives)

while "_" in hidden_word and lives > 0:
    guess = input("Guess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    found = False

    for index in range(len(secret_word)):
        if secret_word[index].lower() == guess:
            hidden_word[index] = secret_word[index]
            found = True

    if not found:
        lives = lives - 1
        print("Wrong guess!")

    print(STAGES[6 - lives])
    print(" ".join(hidden_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Lives:", lives)

if "_" not in hidden_word:
    print("You guessed the word!")
else:
    print("Out of lives! The word was:", secret_word) 
