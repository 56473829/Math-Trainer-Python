from tkinter import Frame 
from tkinter import StringVar
from tkinter import Entry,Label
from Theme import *
from tkinter import messagebox
from Qna import Qna,addData
from time import time

class QuizFrame(Frame):
    def __init__(self, **args):
        super().__init__(**args)
        opt = self.master.children["!frame"].children["!optionframe"]
        self.ques = Qna(opt.basic_check.get()+opt.inter_check.get()+opt.advac_check.get(),
                    opt.level_scale.get())
        self.a = "1234"
        self.b = "1234"
        self.op = "+"
        self.questions_count = opt.ques_scale.get()
        self.curr_q = 0
        self.ans = "2468",
        self.time_scales = []
        self.s_time = 0
        self.e_time = 0
        self.user_ans = StringVar()
        self.qustions_text = StringVar(value="")
        self.user_ans.trace("w",self.doSome)
        self.init_UI()
    
    def intialize(self):
        self.s_time = time()
        opt = self.master.children["!frame"].children["!optionframe"]
        self.ques = Qna(opt.basic_check.get()+opt.inter_check.get()+opt.advac_check.get(),
                    opt.level_scale.get())
        self.questions_count = opt.ques_scale.get()
    
    def init_UI(self):
        qustion = Label(textvariable = self.qustions_text,
                font=question_font,
                bg=primary_color,
                fg=qustion_font_color
                )
        answer = Entry(self,
                font=question_font,
                border=0,bg=primary_color,
                justify="right",
                insertontime=0,
                cursor="arrow",
                width=11,
                textvariable=self.user_ans,
                fg=qustion_font_color,
                )
        answer.focus()
        answer.configure(validate="key", validatecommand=(self.register(self.on_validate), "%P"))
        qustion.grid(pady=(70,0))
        answer.grid()

    def getFormated(self):
        if self.op in "+-÷x":
            a = str(self.a).rjust(10," ")
            b = str(self.b).rjust(10," ")
            return f' {a}\n{self.op}{b}\n{"—"*12}'
        if self.op in "√":
            return f'√{self.a}\n{"—"*12}'
        if self.op in "²³":
            return f'{self.a}{self.op}\n{"—"*12}'

    def on_validate(self,P):
        return P.isdigit() or P == ""

    def doSome(self,*args):
        if self.user_ans.get()==self.ans:
            self.curr_q+=1
            self.user_ans.set("")
            self.getQuiz()
            self.e_time = time()
            self.time_scales+=[int(self.e_time-self.s_time)]
            self.s_time = self.e_time

        if self.curr_q==self.questions_count:
            self.user_ans.set("")
            self.curr_q = 0
            self.master.children['!frame'].grid(row=1,column=0)
            self.master.children["!quizframe"].grid_forget()
            avg = sum(self.time_scales)/self.questions_count
            self.master.children["!frame"].children["!graphframe"].updateGraph(addData(avg))
            messagebox.showinfo("Done !", f"You Done It \n Average Time Required {avg} Seconds")

    def getQuiz(self):
        self.a,self.op,self.b,self.ans= self.ques.giveQustion()
        print("(",self.a,self.op,self.b,self.ans,")")
        self.qustions_text.set(self.getFormated())