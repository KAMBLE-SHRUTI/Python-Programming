class student:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,x,y=0,z=0):
        c=x+y+z
        return c


s=student(12,21)
print(s.add(76,32,6))

