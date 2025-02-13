import random
from hangman_steps import steps
from words import words

def get_valid_words(words):
    word =random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
picked =get_valid_words(words)
# the below print line is to show how the random words are choosen 
# print(picked)
print("the word has this many " ,len(picked), "letters")
for i in range(len(picked)):
    print('-', ' ',end ='')
print()
right = ['_'] * len(picked)
wrong = []
# for the picked right letters
def right_letters():
    for i in right:
        print(i,' ',end='')
    print()

#for the picke wrong letters
def wrong_letters():
    print("the entered letters are the wrong letters",end='')
    for i in wrong:
        print(i,' ',end='')
    print()

#loop of the hangman game{that is to run the game till the man is hanged}
while True:
    guess = input("Guess a letter :").upper()

    if guess in picked:
        index =0
        for i in picked:
            if i==guess:
                right[index] =guess
            index = index + 1
        
        right_letters()
        wrong_letters()
        steps(len(wrong))
    
    elif guess not in picked:
        if guess in wrong:
            print("u guessed it already",guess)
            wrong_letters()
        else:
            print(guess, "the word u have entered is not in my words")
            wrong.append(guess)
            right_letters()
            wrong_letters()
            steps(len(wrong))
#to remove the user chance after the 4th attempt

    if len(wrong)> 4:
        print("Game Over")
        print("picked word",picked)

    if '_' not in right:
        print("Congrats !! You won the game")
        print("picked word is ",picked)
        break