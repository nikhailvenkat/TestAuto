import math
from math import sin, sqrt
class simpleCalc():
    def __init__(self):
        self.val1 = None
        self.val2 = None
    
    def add(self,value1,value2):
        self.val1 = value1
        self.val2 = value2
        return self.val1 + self.val2
    def sub(self,value1,value2):
        self.val1 = value1
        self.val2 = value2
        return self.val1 - self.val2
    def mul(self,value1,value2):
        self.val1 = value1
        self.val2 = value2
        return self.val1 * self.val2
    def div(self,value1,value2):
        self.val1 = value1
        self.val2 = value2
        return self.val1 / self.val2
    def goBack(self):
        return 0
    

class sciCalc(simpleCalc):
    
    
    def sin(self):
        return sin(self.val1)
    def cos(self):
        return cos(self.val1)
    def powerOf(self):
        return pow(self.val1,self.val2)
    def sqRt(self):
        return sqrt(self.val1)
        
    