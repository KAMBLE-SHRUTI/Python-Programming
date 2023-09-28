class computer:
    def __init__(self,**name):
        self.name=name
        #print(self.name)
        for i,j in (self.name).items():
            print(i,j)
        self.processor="intel i5"
        self.os="microsoft window10"
        self.memory="16 GB RAM"
        self.stronge="500 GB"
        self.monitor="LCD mintor"

    def computer_config(self):
        print("computer processor:- ",self.processor)
        print("operating system:- ",self.os)
        print("memory:- ",self.memory)
        print("stronge:- ",self.stronge)
        print("monitor:- ",self.monitor)

a=computer()
a.computer_config()
print("----------------------------------------------------------------------------")
b=computer(processor="intel i3",os="window10",memory="16 GB RAM",strong="512 GB",monitor="24 LCD Monitor" )
