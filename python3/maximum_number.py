#maximun number finding
lst=[89,90,67,56,45,100,56]
maximum_no=lst[0]
for i in range(1,len(lst)):
    if(lst[i]>maximum_no):
        maximum_no=lst[i]
print("maximun number is ",maximum_no)
