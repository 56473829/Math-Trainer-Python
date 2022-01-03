from tkinter import Frame
from tkinter import Label
from Theme import *

class HeaderFrame(Frame):
    def __init__(self,**args):
        super().__init__(**args)

        self.init_UI()
    
    def init_UI(self):
        Label1 = Label(self,text="Math Trainer",
                    font=font_header,
                    background=mid_color,
                    )
        self.columnconfigure(0, weight=1)

        Label1.grid(row=0,column=0,columnspan=1,sticky="we")
    
    def doSome(self,arg=0):
        pass