x = int (input("Enter start of range : "))
y = int(input("Enter end of range : "))
sum = 0
for i in range(x,y+1):
    sum = sum + i

print("Sum = ",sum)