def addition(lst):
    print(lst)
    if(len(lst)==1):
        return lst[0]
    return lst[0]+addition(lst[1:])
a=[12,23,34,45,56,67,98,90]
s=addition(a)
print(s)
