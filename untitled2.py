
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:16:25 2022

@author: shn99
"""

from tkinter import*
from PIL import ImageTk, Image
root=Tk()

root.title("dice")
root.geometry("600x400")

root.configure(background="yellow2")

img=ImageTk.PhotoImage(Image.open ("dice1.4.jpg"))

player1 = Label(root, text = "Player 1", bg="royal blue", fg="White")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg="royal blue",fg="White")
player2.place(relx = 0.9, rely= 0.3, anchor=CENTER)

player_1_score = Label(root, bg="royal blue", fg = "White")
player_1_score.place(relx=0.1, rely=0.4, anchor=CENTER)

player_2_score = Label(root, bg="royal blue", fg = "white")
player_2_score.place(relx=0.5, rely=0.5, anchor=CENTER)


player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(1,6)
    random_dice_label["text"] = "Player 1 Dice Random Number : " + str(random_no)
    player1_score = player1_score + random_no
    player_1_score_label["text"] = str(random_no)
    
    player_1_btn = Button(root, image = img, command = player1)
    player_1_btn.place(relx = 0.1, rely = 0.6, anchor=CENTER)

player2_score = 0
def player2():
    global player2_score
    random_no2 = random.randint(1,6)
    random_dice_label["text"] = "Player 2 Random Number : " + str(player2_score)
    player2_score = player2_score + randomno2
    player_2_score_label["text"] = str(player2_score)
    
    player_2_btn = Button(root, image = img, command = player2)
    player_2_btn.place(relx=0.9, rely=0.6, anchor=CENTER)
    
    
root.mainloop()