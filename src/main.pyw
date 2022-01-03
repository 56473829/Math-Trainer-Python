from tkinter import Tk,Frame
from tkinter import StringVar,IntVar
from SubFrames.GraphFrame import GraphFrame
from SubFrames.HeaderFrame import HeaderFrame
from SubFrames.OptionFrame import OptionFrame
from SubFrames.QuizFrame import QuizFrame
from Theme import *

root = Tk()
root.geometry("700x400")
root.resizable(False,False)
root.config(bg=primary_color)
root.title("Math Trainer")
root.iconbitmap("C:\\Users\\Kuku\\Desktop\\Math Trainer\\src\\res\\mathematics.ico")
root.grid()

root.columnconfigure(0,weight=1)
header = HeaderFrame(master=root, bg=mid_color)
header.grid(row=0,column=0,sticky="nsew")

myFrame = Frame(root,bg=primary_color)

Options = OptionFrame(master=myFrame,bg=primary_color)
Options.grid(row=1,column=0,padx=5,pady=10)

mygraph = GraphFrame(master=myFrame,bg=graph_bg)
mygraph.grid(row=1,column=1,padx=10,pady=10)
myFrame.grid()

myquiz = QuizFrame()

root.mainloop()