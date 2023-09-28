class mobile:
    def config(self):
        print("this is config method from mobile")

class laptop:
    def config(self):
        print("this is config method from method")

class gadgets:
    def electronics(self,obj):
        #print("this is config method from gadgets")
        obj.config()

m=mobile()
l=laptop()
#print("------------------------------------------------------")
g = gadgets()
g.electronics(m)
#g.electronics(l)

