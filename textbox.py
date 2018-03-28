# python3
# -*- coding: utf-8 -*-
"""
These codes will make a window to build text box to entry some text.
"""

import tkinter as tk

window = tk.Tk()
window.title('my tkinter')
window.geometry('200x200')

e = tk.Entry(window,show='1')
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert(0.0,var)

b1 = tk.Button(window,text='insert point',width=15,height=2,command=insert_point)
b1.pack()
b2 = tk.Button(window,text='insert end', command=insert_end)
b2.pack()
    
t = tk.Text(window,height=2)
t.pack()

window.mainloop()
