import tkinter as tk

root = tk.Tk()
root.geometry("451x393")
def change():
    b1.config(text="X")
def change_b2():
    b2.config(text="X")
def change_b3():
    b3.config(text="X")
def change_b4():
    b4.config(text="X")
def change_b5():
    b5.config(text="X")
def change_b6():
    b6.config(text="X")
def change_b7():
    b7.config(text="X")
def change_b8():
    b8.config(text="X")
def change_b9():
    b9.config(text="X")
    

variable = ""
    
b1 = tk.Button(root , width =20 , height=8 , text = variable , command = change)
b1.grid(row=0,column= 0)
b2 = tk.Button(root , width =20 , height=8, text = variable , command = change_b2)
b2.grid(row=1,column= 0)
b3 = tk.Button(root , width =20 , height=8, text = variable , command = change_b3)
b3.grid(row=2,column= 0)

b4 = tk.Button(root , width =20 , height=8, text = variable , command = change_b4)
b4.grid(row=0,column= 1)
b5 = tk.Button(root , width =20 , height=8, text = variable , command = change_b5)
b5.grid(row=1,column= 1)
b6 = tk.Button(root , width =20 , height=8, text = variable , command = change_b6)
b6.grid(row=2,column= 1)

b7 = tk.Button(root , width =20 , height=8, text = variable , command = change_b7)
b7.grid(row=0,column= 2)
b8 = tk.Button(root , width =20 , height=8, text = variable , command = change_b8)
b8.grid(row=1,column= 2)
b9 = tk.Button(root , width =20 , height=8, text = variable , command = change_b9)
b9.grid(row=2,column= 2)
root.mainloop()