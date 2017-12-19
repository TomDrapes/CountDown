#!/usr/bin/env python3


def main():
    words = open('words.txt')
    cd = input("Enter letters: ")
    sixes = []
    sevens = []
    eights = []
    nines = []
    for i in words:
        word = i.strip()
        empty = []
        guess = ""
        for l in cd:
            empty.append(l)
        for letter in word:

            if letter in empty:
                guess += letter
                empty.remove(letter)

        if guess == word and len(word) - 1 == 5:
            sixes.append(word)
        if guess == word and len(word) - 1 == 6:
            sevens.append(word)
        if guess == word and len(word) - 1 == 7:
            eights.append(word)
        if guess == word and len(word) - 1 == 8:
            nines.append(word)

    print("Sixes: ", sixes, "\nSevens: ", sevens, "\nEights: ", eights, "\nNines: ", nines)
    play_again = input("Do you want to go again? (y/n): ")
    if play_again == 'y':
        main()
    elif play_again == 'n':
        exit()

main()


