"""
home
gui
code
information
future

"""
"""
Qustions 
simple +,-
intermidiet /,*
advance sqr,root
"""
from random import randint


class Qna:
    def __init__(self,operation_type,level) -> None:
        self.operation_type = operation_type
        self.level = level

    def giveQustion(self):
        a,b,ans = 0,0,0
        operation = self.operation_type[randint(0,len(self.operation_type)-1)]
        if operation == "+":
            a = randint(0,pow(10,self.level))
            b = randint(0,pow(10,self.level))
            ans = a+b
            if len(str(ans))>10:
                return self.giveQustion(self.operation_type,self.level)
            a,b = max(a,b),min(a,b)
        elif operation == "-":
            a = randint(0,pow(10,self.level))
            b = randint(0,pow(10,self.level))
            a,b = max(a,b),min(a,b)
            ans = a-b
        elif operation == "x":
            a = randint(0,10*self.level)
            b = randint(0,10*self.level)
            a,b = max(a,b),min(a,b)
            ans = a*b
        elif operation == "÷":
            a = randint(0,10*self.level)
            b = randint(1,10*self.level)
            ans = a
            a = a*b
        elif operation == "√":
            a = randint(1,10*self.level)
            ans,a = a,a*a
        elif operation == "²":
            a = randint(1,10*self.level)
            ans = a*a
        elif operation == "³":
            a = randint(1,10*self.level)
            ans = a**3
        a,b,ans = str(a),str(b),str(ans)
        return a,operation,b,ans

def getData():
    FILE = open("C:\\Users\\Kuku\\Desktop\\Math Trainer\\src\\progr.properties")
    filedata = [*map(float,FILE.readline().split(","))]
    FILE.close()
    return filedata

def addData(data):
    new_data = getData()[1:]+[data]
    curr = ",".join([str(i) for i in new_data])
    FILE = open("C:\\Users\\Kuku\\Desktop\\Math Trainer\\src\\progr.properties",'w')
    FILE.write(curr)
    FILE.close()
    return new_data