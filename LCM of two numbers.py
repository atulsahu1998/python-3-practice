x,y=int(input("Enter first number : ")),int(input("Enter second number : "))
lcm=1
i=1
while(x!=1 or y!=1):
    a=x%i
    b=y%i
    if(a==0): 
        x=x/i
    if(b==0):
        y=y/i
    if(a==0 or b==0):
        lcm*=i
    i+=1
    print(lcm)
    