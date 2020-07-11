ntern = int(input("How many terms? "))
li=[]
def fibo(n):
    if(n<0):
        return 0
    elif(n==1):
        return 1
    else:return(fibo(n-1)+fibo(n-2))
if(ntern<1):
    print("Please Enter Value term !!!")
else:
    print("Fibonacci Series ....")
    for n in range(1,ntern+1):
        li.append(fibo(n))
    print(li)