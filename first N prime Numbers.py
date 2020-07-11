i=1
nterm = int(input("How many prime prime numbers : "))
for k in range(1,nterm+1):
    c=0
    for j in range(1,i+1):
        a=i%j
        if(a==0):
            c+=1
    if(c==2):
        print(i)
        
    else:
        k-=1
    i+=1

            
