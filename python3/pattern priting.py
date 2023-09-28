'''
****
****
****
****
'''
for i in range(4):
    for j in range(4):
        print("*", end="")
    print(" ")
         
'''
****
***
**
*
'''
for i in range(4):
    for j in range(4-i):
        print("*", end="")
    print("")

'''
*
**
***
****
'''
for i in range(4):
    for j in range(i+1):
        print("*", end="")
    print("")

'''
*
**
***
****
*****
****
***
**
*
'''

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")
for a in range(5-1):
    for i in range(4-a):
        print("*",end=" ")
    print(" ")
    

     
