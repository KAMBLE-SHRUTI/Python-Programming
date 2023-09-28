#lambda-A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

#addtion
addtion= lambda x,y: x+y
a=addtion(15,20)
print("addition is ",a)

#squre
sqr=lambda x:x*x
b=sqr(12)
print("squre is ",b)

#power
power=lambda x,y:x**y
c=power(2,4)
print("power is ",c)

#finding largest number
largest=lambda x,y:x if(x<y)else y
d=largest (90,12)
print("largest number is ",d)

