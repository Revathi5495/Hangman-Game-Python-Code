# Write your code here
import random
lis = ["python", "java", "swift", "javascript"]
won = 0
lost = 0
print("H A N G M A N\n")
while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    inpt = input()
    if inpt == "play":
        bol = 8
        word = random.choice(lis) # random word from list
        length = len(word) # length of the random word
        hypword = length * '-' # guessing word
        guess = False
        guessed_word = ''
        while bol > 0:
            if hypword.count('-') == 0:
                guess = True
                print("You guessed the word",word+'!',"\nYou survived!")
                won += 1
                break
            print(hypword)
            ch = input("Input a letter:") # player uncovering letter
            if len(ch) == 0 or len(ch) >= 2:
                print("Please, input a single letter.\n")
                continue
            elif not ch.islower():
                print("Please, enter a lowercase letter from the English alphabet.\n")
                continue
            elif (ch in hypword) or (ch in guessed_word) :
                print("You've already guessed this letter\n")
            else:
                if ch in hypword: # checks if letter is already guessed 
                    print("You've already guessed this letter.\n")
                elif ch in word:  # checking if letter is in random word
                    print()
                    for i in range(len(word)):  # placing letter at desired index with hyphens too
                        if word[i] == ch:
                            hypword = hypword[:i] + ch + hypword[i+1:] #concatenating letter with hyphens 
                else:
                    guessed_word += ch
                    print("That letter doesn't appear in the word.\n")
                    bol -=1
        if guess == False:
            print("You lost!")    
            lost += 1
            continue
    elif(inpt=="results"):
        print("You won:",won,"times.")
        print("You lost:",lost,"times.")
    else:
        exit()