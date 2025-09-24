import tkinter as tk
from tkinter import messagebox as tmsg
import time

root = tk.Tk()
root.geometry("451x393")
root.maxsize(451,393)
root.title("Tic Tac Toe")

turn = 'X'

def check_win():
    if b1['text'] == b2['text'] == b3['text'] != "":
        print("You won!")
        yesno = tmsg.askquestion(" Wohoo !","You Won ! want Rematch ?")
        if yesno == 'yes':
            reset()
        else:
            time.sleep(5)
            root.quit()

    if b4['text'] == b5['text'] == b6['text'] != "":
        print("You won!")
        yesno = tmsg.askquestion("Wohoo !","You Won ! want Rematch ?")
        if yesno == 'yes':
            reset()
        else:
            time.sleep(5)
            root.quit()
        
    if b7['text'] == b8['text'] == b9['text'] != "":
        print("You won!")
        yesno = tmsg.askquestion("Wohoo !","You Won ! want Rematch ?")
        if yesno == 'yes':
            reset()
        else:
            time.sleep(5)
            root.quit()
        
    if b1['text'] == b4['text'] == b7['text'] != "":
        print("You won!")
        yesno = tmsg.askquestion("Wohoo !","You Won ! want Rematch ?")
        if yesno == 'yes':
            reset()
        else:
            time.sleep(5)
            root.quit()
        
    if b2['text'] == b5['text'] == b8['text'] != "":
        print("You won!")
        yesno = tmsg.askquestion("Wohoo !","You Won ! want Rematch ?")
        if yesno == 'yes':
            reset()
        else:
            time.sleep(5)
            root.quit()
       
    if b3['text'] == b6['text'] == b9['text'] != "":
        print("You won!")
        yesno = tmsg.askquestion("Wohoo !","You Won ! want Rematch ?")
        if yesno == 'yes':
            reset()
        else:
            time.sleep(5)
            root.quit()
    
    if b1['text'] == b5['text'] == b9['text'] != "":
        print("You won!")
        yesno = tmsg.askquestion("Wohoo !","You Won ! want Rematch ?")
        if yesno == 'yes':
            reset()
        else:
            time.sleep(5)
            root.quit()

    if b3['text'] == b5['text'] == b7['text'] != "":
        print("You won!")
        yesno = tmsg.askquestion(" Wohoo !","You Won ! want Rematch ?")
        if yesno == 'yes':
            reset()
        else:
            time.sleep(5)
            root.quit()
        

def change(button):
    global turn
    if button['text'] == "":
        button.config(text=turn)
        check_win()
        turn = 'O' if turn == 'X' else "X"

def reset():
    for buttons in (b1,b2,b3,b4,b5,b6,b7,b8,b9):
        buttons.config(text="")


    
    
b1 = tk.Button(root , width =20 , height=8 , text = "" ,command =lambda:  change(b1))
b1.grid(row=0,column= 0)
b2 = tk.Button(root , width =20 , height=8   , text = "", command =lambda: change(b2))
b2.grid(row=1,column= 0)
b3 = tk.Button(root , width =20 , height=8  , text = "", command =lambda: change(b3))
b3.grid(row=2,column= 0)

b4 = tk.Button(root , width =20 , height=8  , text = "", command =lambda: change(b4))
b4.grid(row=0,column= 1)
b5 = tk.Button(root , width =20 , height=8  , text = "", command =lambda: change(b5))
b5.grid(row=1,column= 1)
b6 = tk.Button(root , width =20 , height=8  , text = "", command =lambda: change(b6))
b6.grid(row=2,column= 1)

b7 = tk.Button(root , width =20 , height=8  , text = "", command =lambda: change(b7))
b7.grid(row=0,column= 2)
b8 = tk.Button(root , width =20 , height=8 , text = "", command =lambda: change(b8))
b8.grid(row=1,column= 2)
b9 = tk.Button(root , width =20 , height=8  , text = "", command =lambda: change(b9))
b9.grid(row=2,column= 2)



root.mainloop()

