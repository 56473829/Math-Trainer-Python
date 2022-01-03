from tkinter import Frame, LabelFrame
from tkinter import StringVar, IntVar
from tkinter import Button, Checkbutton, Scale
from Theme import *

class OptionFrame(Frame):
    def __init__(self,**args):
        super().__init__(**args)
        self.basic_check = StringVar()
        self.basic_check.set("+-")
        self.inter_check = StringVar()
        self.advac_check = StringVar()
        self.level_scale =  IntVar()
        self.ques_scale =  IntVar()

        self.init_UI()
    
    def init_UI(self):
        start = Button(self,text="START",
                       height=3,
                       width=14,
                       borderwidth=3,
                       fg=font_color,
                       bg=primary_color,
                       activebackground=secondary_color,
                       font=font_primary,
                       command=self.startTraining
                       )
        
        label_frame = LabelFrame(self,
                    text ='Options',
                    font=font_10b,
                    bg=primary_color,
                    fg=font_color
                    )

        check_button1 = Checkbutton(label_frame, 
                    text = "BASIC",
                    variable = self.basic_check,
                    onvalue = "+-",
                    offvalue = "",
                    bg=primary_color,
                    activebackground=primary_color,
                    selectcolor=primary_color,
                    fg=font_color,
                    )
        check_button2 = Checkbutton(label_frame, 
                    text = "INTERMIDIATE",
                    variable = self.inter_check,
                    onvalue = "x÷",
                    offvalue = "",
                    bg=primary_color,
                    activebackground=primary_color,
                    selectcolor=primary_color,
                    fg=font_color,
                    )

        check_button3 = Checkbutton(label_frame, 
                    text = "ADVANCE",
                    variable = self.advac_check,
                    onvalue = "√²³",
                    offvalue = "",
                    bg=primary_color,
                    activebackground=primary_color,
                    selectcolor=primary_color,
                    fg=font_color,
                    )

        Scale1 = Scale(label_frame,
                    variable=self.level_scale,
                    orient='horizontal',
                    from_=1,to=10,
                    label="Difficulty",
                    bg=primary_color,
                    activebackground=primary_color,
                    fg=font_color,
                    highlightbackground=secondary_color
                    )
        Scale1.set(2)

        Scale2 = Scale(label_frame,
                    variable=self.ques_scale,
                    orient='horizontal',
                    from_=10,to=50,
                    label="Questions",
                    bg=primary_color,
                    activebackground=primary_color,
                    fg=font_color,
                    highlightbackground=secondary_color
                    )

        start.grid(row=0,column=0,padx=10,pady=10)
        label_frame.grid(row=2,column=0,sticky='W',padx=20)
        check_button1.grid(row=2,column=0,sticky='W',padx=20)
        check_button2.grid(row=3,column=0,sticky='W',padx=20)
        check_button3.grid(row=4,column=0,sticky='W',padx=20,pady=5)
        Scale1.grid(row=5,column=0,sticky='W',padx=20)
        Scale2.grid(row=6,column=0,sticky='W',padx=20,pady=10)
    
    def startTraining(self):
        self.master.master.children["!quizframe"].grid()
        self.master.master.children['!frame'].grid_forget()
        self.master.master.children["!quizframe"].children["!entry"].focus()
        self.master.master.children["!quizframe"].intialize()
        self.master.master.children["!quizframe"].getQuiz()