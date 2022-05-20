from nltk.corpus import words
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
import random
ans = 0
db = open("wordle_db.txt", 'r+').read().splitlines()
wordStr = random.choice(db)
while wordStr not in words.words():
    wordStr = random.choice(db)
word = [x for x in wordStr]
t = 0
while t < 6:
    hint = []
    askGuess = "Enter your guess #" + str(t+1) + ": "
    guessStr = input(askGuess)
    if wnl.lemmatize(guessStr) in words.words():
        t += 1
        guess = [y for y in guessStr]
        for i in guess:
            if i == word[guess.index(i)]:
                hint.append("🟩")
            elif i in word:
                hint.append("🟨")
            else:
                hint.append("⬛")
        print(' '.join(hint))
        if hint == ["🟩", "🟩", "🟩", "🟩", "🟩"]:
            ans = 1
            print("Correct Answer!")
            break
    else:
        print("This is not a valid word, please try again. Press enter to guess again.")
        guessStr = input()
if not ans:
    print("The word was " + wordStr + "! Better luck next time!")