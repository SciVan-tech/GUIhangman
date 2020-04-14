from PIL import ImageTk, Image
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import time
import random
from tkinter import *
import sys
sys.setrecursionlimit(10**6)
import os

file = ""
W_list = []
G_list = []
C_list = []
W = ""

def pick_word(Word_length):
    global W_list
    global G_list
    global W
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        W_list.append(line_list)

    N = random.randint(0, int(len(W_list)))
    temp_word = str(W_list[N])
    W = temp_word[2:int(len(temp_word))-2]
    if int(len(W)) == Word_length:
        W_list = list(W)
        print(W_list)
        G_list = ['_'] * len(W)
        print(G_list)
    else:
        pick_word(Word_length)

def play(k):
        global G_list
        global W_list
        global W
        print(W_list)
        if len(k) > 1 and k == W:
            G_list=("Correct!!!!")
            print(W_list)
        elif len(k) > 1 and k != W:
            print("Wrong Word")
        elif len(k) == 1:
            for i in range(len(W)):
                if k == str(W_list[i]) and str(G_list[i]) == "_":
                    index = W_list.index(str(k))
                    # print(index)
                    G_list[int(i)] = str(k.upper())
        else:
            pass
        print(G_list)


class MyWindow:
    def __init__(self, win):
        self.point=1
        self.lbl1 = Label(win, text="Word length", font=("Arial", 12))
        self.lbl2 = Label(win, text='Guess', font=("Arial", 12))
        self.lbl3 = Label(win, text='', font=("Arial", 60))
        self.lbl4 = Label(win, text='', font=("Arial", 60))
        self.t1 = Entry()
        self.t2 = Entry()
        self.lbl1.place(x=120, y=50)
        self.t1.place(x=400, y=60, anchor="center")
        self.lbl2.place(x=400, y=120, anchor="center")
        self.t2.place(x=400, y=100, anchor="center")
        self.b1 = Button(win, text='Pick it!', bd=1,fg="green", command=self.Submit)
        self.b1.place(x=600, y=50)
        self.b2 = Button(win, text='PLAY', bd=1, fg="red", command=self.Game)
        self.b2.place(x=400, y=150, anchor="center")
        self.lbl3.place(x=400, y=300, anchor="center")
        self.lbl4.place(x=700, y=30,)
        self.lbl5 = Label(win, text="", font=("Arial", 20))
        self.lbl5.place(x=400, y=180, anchor="center")
        self.b3 = Button(win, text='ITA',  bd=1, fg="black",
                         command=self.Ita, font="Verdana 22 bold", width=15)
        self.b3.place(x=200, y=300, anchor="center")
        self.b4 = Button(win, text='ENG',  bd=1, fg="black",
                         command=self.Eng, font="Verdana 22 bold", width = 15)
        self.b4.place(x=600, y=300, anchor="center")
        self.lbl6 = Label(win, text="", font=("Arial", 20))
        self.lbl6.place(x=5, y=5)

    def Ita(self):
        global file
        file = open("WordListITA.txt", "r")
        self.b3.destroy()
        self.b4.destroy()
        self.lbl6.config(text='Italiano')


    def Eng(self):
        global file
        file = open("WordList.txt", "r")
        self.b3.destroy()
        self.b4.destroy()
        self.lbl6.config(text='English')

    def Submit(self):
        len_word = self.t1.get()
        # if str(type(len_word)) != 'int':
        #     self.lbl3.config(text='NUMBERS only!')
        if int(len_word) > 12:
            self.lbl3.config(text='Too LONG!')
        elif int(len_word) < 3:
            self.lbl3.config(text='Too SHORT!')
        else:
            pick_word(int(len_word))
            self.t1.destroy()
            self.b1.destroy()
            self.lbl1.destroy()
            self.lbl3.config(text=' '.join(G_list))

    def Game(self):
        global C_list
        lett = str(self.t2.get())
        if lett == "":
            self.t2.delete(first=0, last=100)
            self.lbl3.config(text='No letter!')
        elif lett in C_list:
            self.t2.delete(first=0, last=100)
            self.lbl3.config(text='Called Letter!')
            self.lbl5.config(text='-'.join(C_list))
        else:
            play(lett)
            C_list.append(lett)
            self.t2.delete(first=0, last=100)
            self.lbl3.config(text=' '.join(G_list))
            self.lbl4.config(text=self.point)
            self.lbl5.config(text='-'.join(C_list))
            self.point+=1

window = Tk()
mywin = MyWindow(window)
window.title('GHangman')
window.geometry("800x350")
window.mainloop()
