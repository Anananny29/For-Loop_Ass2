x = int (input("Enter start of range : "))
y = int(input("Enter end of range : "))

for i in range(x,y+1):
    if(i%2==0):
        print(i)