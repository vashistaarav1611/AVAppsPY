import turtle
import tkinter as tk
turtle.title("Drawing")
t = turtle.Pen()
t.shape("turtle")
w1 = tk.Tk()
w1.title("Drawing App by Aarav Vashist")
def up():
  t.fd(10)
def left():
  t.left(10)
def right():
  t.right(10)
def back():
  t.bk(10)
def pu():
  t.penup()
  t.shape("square")
def pd():
  t.pendown()
  t.shape("turtle")
def sf():
  t.shape("arrow")
  t.begin_fill()
def ef():
  t.end_fill()
  t.shape("turtle")
###
label1=tk.Label(w1,text="Drawing App")
clic1 = tk.Button(w1,text="up↑",command=up)
clic2 = tk.Button(w1,text="left←",command=left)
clic3 = tk.Button(w1,text="right→",command=right)
clic4 = tk.Button(w1,text="backward↓",command=back)
b5 = tk.Button(w1,text="up✎",bg="white",command=pu)
b6 = tk.Button(w1,text="down✎",bg="white",command=pd)
b7 = tk.Button(w1,text="start fill✎",command=sf)
b8 = tk.Button(w1,text="end fill✎",command=ef)
###
label1.pack()
clic1.pack()
clic2.pack()
clic3.pack()
clic4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()
