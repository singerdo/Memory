class count:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def plus(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def multi(self):
        return self.a*self.b

a=count(1,3)
print(a.multi())
print(a.sub())