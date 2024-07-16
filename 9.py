count = 0
x = int(input("Enter start of the range : "))
y = int(input("Enter end of the range : "))

for i in range(x,y+1):
    if(i<0):
        count = count + 1 

print("Total number of negative numbers : ",count)
