#golbal fuction

def addition():
    global a,b
    a=20
    b=30
    #a=40
    #b=30
    print("addition is ",a+b)

def substraction():
    print(a-b)
addition()
substraction()
