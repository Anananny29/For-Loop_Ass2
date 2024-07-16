x = int(input("Enter a number : "))
y = int(input("Enter a number : "))



for i in range(x,y):
    if(i%3==0 and i%5==0):
        print(i)
