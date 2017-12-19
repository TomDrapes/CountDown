#!/usr/bin/env python3

from tkinter import*
from tkinter import ttk
import random

root = Tk()
root.title("Agraman")


frame = ttk.Frame(root, padding='3 3 3 3')
frame.grid(column=0, row=0, sticky=(N, S, E, W))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
"""Letters Round"""
count = 0
sec = 60
anagram = []

"""Numbers Round"""
seconds = 60


current = "0"
op = ""
a = 0
b = 0
varA = 0
varB = 0
t = False
clock = 0

def game2():

    frame4 = ttk.Frame(root, padding='3 3 3 3')
    frame4.grid(column=0, row=0, sticky=(N, S, E, W))
    frame4.columnconfigure(0, weight=1)
    frame4.rowconfigure(0, weight=1)

    bigNumbers = [100, 75, 50, 25]
    smallNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    randomNumbers = random.sample(bigNumbers, 2) + random.sample(smallNumbers, 4)
    targetNumber = random.randint(101, 999)

    def num_press(num, button):
        button.configure(state=DISABLED)
        sum_label['text'] = num
        global a
        global b
        if a == 0:
            a = num
        else:
            b = num



    def operator(x):
        global op
        op = x


    def equals(op):
        global current
        global a
        global b


        if op == "+":
            a += b
            current = a
            b = 0
            sum_label['text'] = a

        elif op == "-":
            a -= b
            current = a
            b = 0
            sum_label['text'] = a

        elif op == "*":
            a *= b
            current = a
            b = 0
            sum_label['text'] = a

        elif op == "/":
            a /= b
            current = a
            b = 0
            sum_label['text'] = a


    def clear():
        sum_label['text'] = 0
        global a
        global b
        a = 0
        b = 0
        button1.configure(state=NORMAL)
        button2.configure(state=NORMAL)
        button3.configure(state=NORMAL)
        button4.configure(state=NORMAL)
        button5.configure(state=NORMAL)
        button6.configure(state=NORMAL)
        storeVar_a['text'] = "A"
        storeVar_b['text'] = "B"
        storeVar_a.configure(state=NORMAL)
        storeVar_b.configure(state=NORMAL)

    def store():
        global a
        global b
        a = 0
        b = 0
        if storeVar_a['text'] is 'A':
            storeVar_a['text'] = current
            global varA
            varA = current
        else:
            storeVar_b['text'] = current
            global varB
            varB = current

    def submit(current, targetNumber):
        global count
        global seconds
        global t
        global clock
        final = int(current)
        final_target = int(targetNumber)
        x = int(targetNumber - 10)
        y = int(targetNumber + 10)

        if final == final_target:
            sum_label['text'] = "You Win"
            count += 10
            seconds = 60
            time_label2.after_cancel(clock)
            score2()

        elif x <= final <= y:
            sum_label['text'] = "Close Enough"
            count += 5
            seconds = 60
            time_label2.after_cancel(clock)
            score2()

        else:
            sum_label['text'] = "Try Again"

    def timer2():
        global seconds
        global clock
        seconds -= 1
        time_label2['text'] = seconds
        clock = time_label2.after(1000, timer2)

        if seconds is 0:
            seconds = 60
            time_label2.after_cancel(clock)
            score2()

    def score2():

        frame3 = ttk.Frame(root, padding='3 3 3 3')
        frame3.grid(column=0, row=0, sticky=(N, S, E, W))
        frame3.columnconfigure(0, weight=1)
        frame3.rowconfigure(0, weight=1)

        score_label = ttk.Label(frame3, text="Score!", font=("Courier", 34), justify=CENTER)
        score_label.grid(column=0, columnspan=3, row=1)
        points2_label = ttk.Label(frame3, text=count, font=("Courier", 44), justify=CENTER)
        points2_label.grid(column=0, columnspan=3, row=2)
        new_game = ttk.Button(frame3, text='Next Round', command=start)
        new_game.grid(column=0, columnspan=3, row=3)
        misc_label2 = ttk.Label(frame3, text='Out of time!', font=("Courier", 44))
        misc_label2.grid(column=0, columnspan=3, row=0)

    """Buttons and Labels"""

    button1 = ttk.Button(frame4, text=randomNumbers[0], command=lambda: num_press(randomNumbers[0], button1))
    button1.grid(column=0, row=3)

    button2 = ttk.Button(frame4, text=randomNumbers[1], command=lambda: num_press(randomNumbers[1], button2))
    button2.grid(column=1, row=3)

    button3 = ttk.Button(frame4, text=randomNumbers[2], command=lambda: num_press(randomNumbers[2], button3))
    button3.grid(column=0, row=4)

    button4 = ttk.Button(frame4, text=randomNumbers[3], command=lambda: num_press(randomNumbers[3], button4))
    button4.grid(column=1, row=4)

    button5 = ttk.Button(frame4, text=randomNumbers[4], command=lambda: num_press(randomNumbers[4], button5))
    button5.grid(column=0, row=5)

    button6 = ttk.Button(frame4, text=randomNumbers[5], command=lambda: num_press(randomNumbers[5], button6))
    button6.grid(column=1, row=5)

    addition = ttk.Button(frame4, text="+", command=lambda: operator("+"))
    addition.grid(column=2, row=3)

    minus = ttk.Button(frame4, text="-", command=lambda: operator("-"))
    minus.grid(column=2, row=4)

    multiply = ttk.Button(frame4, text="x", command=lambda: operator("*"))
    multiply.grid(column=3, row=3)

    divide = ttk.Button(frame4, text=chr(247), command=lambda: operator("/"))
    divide.grid(column=3, row=4)

    Equals = ttk.Button(frame4, text="=", command=lambda: equals(op))
    Equals.grid(column=2, row=5)

    targetNum = ttk.Label(frame4, text=targetNumber, justify=CENTER, font=("Courier", 44))
    targetNum.grid(column=1, row=0, columnspan=2)

    sum_label = ttk.Label(frame4, text=current, justify=CENTER, font=("Courier", 24))
    sum_label.grid(column=1, columnspan=2, row=1)

    clearz = ttk.Button(frame4, text="CLEAR", command=lambda: clear())
    clearz.grid(column=3, row=2)

    storeVar_a = ttk.Button(frame4, text='A', command=lambda: num_press(varA, storeVar_a))
    storeVar_a.grid(column=0, row=2)

    storeVar_b = ttk.Button(frame4, text='B', command=lambda: num_press(varB, storeVar_b))
    storeVar_b.grid(column=1, row=2)

    submit_btn = ttk.Button(frame4, text='SUBMIT', command=lambda: submit(current, targetNumber))
    submit_btn.grid(column=3, row=5)

    storeVar_label = ttk.Button(frame4, text='STORE', command=lambda: store())
    storeVar_label.grid(column=2, row=2)

    time_label2 = ttk.Label(frame4, text=seconds, justify=CENTER, font=("Courier", 34))
    time_label2.grid(column=0, columnspan=1, row=1)
    time_label2.pack()

    timer2()
    clear()
    for child in frame4.winfo_children():
        child.grid_configure(padx=5, pady=5)


def start():

    anagram = []
    global sec
    sec = 60
    frame2 = ttk.Frame(root, padding='3 3 3 3')
    frame2.grid(column=0, row=0, sticky=(N, S, E, W))
    frame2.columnconfigure(0, weight=1)
    frame2.rowconfigure(0, weight=1)
    """This stores the shuffled consonants and vowels in part_3 which is the anagram"""
    vowels = "aeiou"
    consonants = 'bbccddffgghhjjkkllmmnnppqrrssttvvwwxyz'
    part_1 = random.sample(vowels, 4)
    part_2 = random.sample(consonants, 5)
    part_3 = part_1 + part_2
    random.shuffle(part_3)
    anagram_label = ttk.Label(frame2, text=part_3, justify=CENTER, font=("Courier", 24))
    anagram_label.grid(column=0, columnspan=3, row=2)
    for letter in part_3:
        anagram.append(letter)
    answer = StringVar()
    guessed_words = []

    def gobutton(*args):
        """This is assigned to the return key and starts the timer the first time the 'GO' button is pressed
        It also calls possible_words to check user input."""
        possible_words(anagram, guessed_words)
        answer_entry.delete(0, END)

    def score():

        time_label.grid_remove()
        frame3 = ttk.Frame(root, padding='3 3 3 3')
        frame3.grid(column=0, row=0, sticky=(N, S, E, W))
        frame3.columnconfigure(0, weight=1)
        frame3.rowconfigure(0, weight=1)

        score_label = ttk.Label(frame3, text="Score!", font=("Courier", 34), justify=CENTER)
        score_label.grid(column=0, columnspan=3, row=1)
        points2_label = ttk.Label(frame3, text=count, font=("Courier", 44), justify=CENTER)
        points2_label.grid(column=0, columnspan=3, row=2)
        new_game = ttk.Button(frame3, text='Next Round', command=game2)
        new_game.grid(column=0, columnspan=3, row=3)
        misc_label2 = ttk.Label(frame3, text='Out of time!', font=("Courier", 44))
        misc_label2.grid(column=0, columnspan=3, row=0)

        for child in frame3.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def timer():
        """This counts time and ends game after certain point"""
        #time_label.configure(state=NORMAL)
        global sec
        sec -= 1
        time_label['text'] = sec
        clock = time_label.after(1000, timer)

        if sec == 0:

            sec = 60
            time_label.after_cancel(clock)
            score()

    def possible_words(anagram, guessed_words):
        """This checks user input against words in dictionary and against the letters in the anagram
        as well as words already guessed. It also assigns points depending on the length of the word"""
        words_list = open('words.txt')
        anagram2 = anagram
        answer2 = answer.get()

        for l in answer2:
            if l not in anagram2:
                misc_label['text'] = "Not in anagram"
                break
            else:
                pass

            for i in words_list:
                wordz = i.strip()
                word = str(wordz)
                if answer.get() not in guessed_words:
                    if word == answer.get():
                        misc_label['text'] = (answer2 + " is in the dictionary! ")
                        points = len(answer2)
                        global count
                        count += points
                        count_label['text'] = ("Points: " + str(count))
                        guessed_words.append(answer2)
                        break

    """All my labels"""
    title_label = ttk.Label(frame2, text="Agra-Man", font=("Courier", 44))
    title_label.grid(column=0, columnspan=3, row=1, sticky=N)

    time_label = ttk.Label(frame2, text=sec, justify=CENTER, font=("Courier", 34))
    time_label.grid(column=0, row=7)
    time_label.pack()

    count_label = ttk.Label(frame2, text=("Points: " + str(count)), font=("Courier", 24), justify=CENTER)
    count_label.grid(column=0, columnspan=1, row=3)

    answer_entry = ttk.Entry(frame2, width=7, textvariable=answer)
    answer_entry.grid(column=0, row=4, sticky=(W, E))

    misc_label = ttk.Label(frame2, text="", justify=CENTER)
    misc_label.grid(column=0, columnspan=3, row=6)

    go_button = ttk.Button(frame2, width=7, text="Go", command=(gobutton))
    go_button.grid(column=0, row=5, sticky=(W, E))

    root.bind('<Return>', gobutton)

    answer_entry.focus()

    timer()

    for child in frame2.winfo_children():
        child.grid_configure(padx=5, pady=5)


start_game = ttk.Button(frame, text='Start Game', command=start)
start_game.grid(column=0,  row=3)

welcome_label = ttk.Label(frame, text='AGRAMAN\nThe Letters\nand\nNumbers Game', justify=CENTER, font=("Courier", 44))
welcome_label.grid(column=0, columnspan=3, row=0)



root.mainloop()



