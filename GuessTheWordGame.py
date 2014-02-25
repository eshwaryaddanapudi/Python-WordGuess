import random

def get_random_word():
    words = ["pizza","Burger", "Dominos","puri","donut"]
    word = words[random.randint(0,len(words) -1)]
    return word

def show_space_characters(blankedWord):
    for char in blankedWord:
        print(char," ", end="")
    print("");

def get_guess_from_user():
    print("guess a letter..")
    return input()


def process_input_letter(inputLetter,secretWord,blankedWord):
    comparedOutput = False
    for i in range(0,len(secretWord)):
        if secretWord[i] == inputLetter:
            comparedOutput = True
            blankedWord[i]= inputLetter


    return comparedOutput


def play_word_game():
    print("get, set, Go!")
    strikes = 0
    maxStrikes = 3
    playing = True


    randomWord = get_random_word()
    blankedWord = list("_" * len(randomWord))
    
    while playing:
        show_space_characters(blankedWord)
        letter = get_guess_from_user()
        foundLetter = process_input_letter(letter,randomWord,blankedWord)

        if not foundLetter:
            strikes += 1
            print("strikes left:")
            print((maxStrikes - strikes),maxStrikes)

        if not "_" in blankedWord:
            playing = False

            
        if strikes>=maxStrikes:
            print("max changes exceeded")
            playing = False

    if playing == False and strikes >= maxStrikes:
        print("Loser..")
    else:
        print("winner")    
        
    
print("Game Started")
play_word_game()
print("Game Ended")
