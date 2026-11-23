import sys

STAGES = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
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
    secret_word = sys.argv[1]
else:
    secret_word = input("Enter the word to guess: ")

hidden_word = ["_" for _ in secret_word]
lives = 6

print(STAGES[6 - lives])
print(" ".join(hidden_word))
print("Lives:", lives)

while "_" in hidden_word and lives > 0:
    guess = input("Guess a letter: ")
    found = False

    for index in range(len(secret_word)):
        if secret_word[index].lower() == guess.lower():
            hidden_word[index] = secret_word[index]
            found = True

    if not found:
        lives = lives - 1
        print("Wrong guess!")

    print(STAGES[6 - lives])
    print(" ".join(hidden_word))
    print("Lives:", lives)

if "_" not in hidden_word:
    print("You guessed the word!")
else:
    print("Out of lives! The word was:", secret_word)
