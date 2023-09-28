class  demo1:
    def test(self):
        print("this is test method from demo1")

class demo2(demo1):
    def test1(self):
        print("this is test1 method from demo2")

    def test2(self):
        print("this is test2 method from demo2")

a=demo2()
a.test()