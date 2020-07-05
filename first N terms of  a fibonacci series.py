nterm = int(input('How many terms your want to see ? :'))
def fib(n):
    if n<1:
        return 0
    elif n==1:
        return 1
    else:
        return(fib(n-1) + fib(n-2))
if nterm < 1:
    print("Please Enter Valid Number..")
else:
    print("Fibonacci Series..")
    for i in range(nterm):
        print(fib(i))