import tkinter as tk

root = tk.Tk()
root.geometry("451x393")
root.maxsize(451,393)

turn = 'X'

def change(button):
    global turn
    if button['text'] == "":
        button.config(text=turn)
        turn = 'O' if turn == 'X' else "X"

    
    
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

