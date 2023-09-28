#prime number using while loop
a=0
i=2
j=int(input("enter your value"))
while(i<=j):
    if(j%i==0):
        a=1
        break
    i=i+1
if(a==0):
    print("prime",i)
else:
    print("composite",i)


#prime number using for loop
a=int(input("enter your value"))
b=a//2
state=0
for i in range(2,a):
    if(a%i==0):
        state=i
        break
if(state==1):
    print("not prime")
else:
    print("prime")

