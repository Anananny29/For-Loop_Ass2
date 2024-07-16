x = input("Enter a character : ")
y = input("Enter a character : ")

if (len(x) ==1 and len(y)==1 and ord(x)<=ord(y)):
    for i in range(ord(x),ord(y)):
        print("ASCII value of",chr(i),"is",i)
