a,b = int(input("Enter first number : ")), int(input("Enter second number : "))
if(a>b):
    big=a
else:big=b
for i in range(2,big):
    if(a%i==0 and b%i==0):

        print("are not co-primes ")
        break
print(" are  co_primes ")

