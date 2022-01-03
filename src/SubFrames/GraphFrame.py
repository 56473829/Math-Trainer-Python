from tkinter import Frame,Label
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy.lib.function_base import delete
from Theme import *
from Qna import getData

class GraphFrame(Frame):
    def __init__(self,**args):
        super().__init__(**args)
        self.dataY = getData()
        self.dataX = ["Last\n Attempt"]
        for i in range(len(self.dataY)-1):
            self.dataX = [" "*i] + self.dataX
        self.bg_color = graph_bg
        self.ylabel = "Average Time(Sec)"
        self.init_UI()
    
    def init_UI(self):

        label = Label(self, text ='Performace', font = font_secondary ,background=self.bg_color)
        label.pack()

        self.fig = Figure(figsize = (6, 4),
                     dpi = 80,
                     facecolor=self.bg_color
                    )
        self.graph = self.fig.add_subplot(111)
        self.graph.plot(self.dataX,self.dataY,"-o",color="#11ee11")
        self.graph.set_ylabel(self.ylabel)
        self.graph.set_facecolor(self.bg_color)
        self.graph.spines['top'].set_visible(False)
        self.graph.spines['right'].set_visible(False)
        self.graph.spines['bottom'].set_visible(False)
        self.canvas = FigureCanvasTkAgg(self.fig,master = self)
        self.canvas.draw()
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack()

    def updateGraph(self,dataY):
        self.dataY = dataY
        self.widget.pack_forget()
        self.fig.clf()
        self.graph = self.fig.add_subplot(111)
        self.graph.plot(self.dataX,self.dataY,"-o",color="#11ee11")
        self.graph.set_ylabel(self.ylabel)
        self.graph.set_facecolor(self.bg_color)
        self.graph.spines['top'].set_visible(False)
        self.graph.spines['right'].set_visible(False)
        self.graph.spines['bottom'].set_visible(False)
        self.canvas = FigureCanvasTkAgg(self.fig,master = self)
        self.canvas.draw()
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack()

