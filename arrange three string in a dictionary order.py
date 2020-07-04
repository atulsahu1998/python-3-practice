e=97
a=input("Enter fist string : ")
b=input("Enter second string : ")
x=input("Enter therd string : ")
for e in range(2):
    if (ord(a[0])>=ord(b[0]) and ord(a[0])>=ord(x[0])):
        print(a)
    elif (ord(b[0])>=ord(x[0])):
        print(b)
    else:
        print(x)
