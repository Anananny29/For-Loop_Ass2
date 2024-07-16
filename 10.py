x = int(input("Enter start of the range : "))
y = int(input("Enter end of the range : "))

mul=1

for i in range(x,y+1):
    if(i%2==1):
        mul = mul*i

print("Product :",mul)