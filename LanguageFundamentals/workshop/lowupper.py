num=int(input("enter the number"))
low=int(input("enter lower"))
upper=int(input("enter upper"))
for i in range(1,(upper+1)):
    if i**num in range(low,(upper+1)):
        print(i**num)
    else:
        pass