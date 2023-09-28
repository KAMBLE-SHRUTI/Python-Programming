print("_________assignment no 1:_________")
def num():
    sum=0
    a=[12,23,34,65,67]
    for i in a:
        sum=sum+i
    return sum
n=num()
print("addition",n)
precentage=n/5
print(precentage)
    
print("_________assignment no 2:_________")
def marks():
    sum=0
    for i in range(5):
        m=int(input("enter your marks: "))
        
        sum=sum+m
    return sum
n=marks()
print("marks of addition",n)
d=n/5
print("precentage",d)

print("________assignment no 3 :_______")
def biling_application():
    sum=0
    for i in range(400):
        a=int(input("product value: "))
        b=raw_input("do you want to cantinue? ")
        sum=sum+a
        if(b=="no"):
            break
    if(sum>100 and sum<=500):
        print("payable amount")
        dis=sum*0.05
        amount=sum-dis
        
    elif(sum>500 and sum<=1000):
        print("payable amount")
        dis=sum*0.10
        amount=sum-dis
        
    elif(sum>1000 and sum<=1500):
        print("payable amount")
        dis=sum*0.15
        amount=sum-dis
        
    elif(sum>1500 and sum<=2000):
        print("payable amount")
        dis=sum*0.20
        amount=sum-dis
    return amount
c=biling_application()
print(c)

    
    
        


    
