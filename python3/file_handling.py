#create a new file
file=open("computer.txt","U")

#wiriting mode
file=open("computer.txt","w")
file.write("python \n")
file.write(" i love python")
file.close()

#reading mode
file=open("computer.txt","r")
print(file.read())

#readlines()fuction
file=open("computer.txt","r")
print(file.readlines(2))
file.close()

