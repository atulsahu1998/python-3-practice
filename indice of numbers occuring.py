li=[1,2,3,4,5,1,3,5,1,5,3,2,5]
count=0
print(li)
index = int(input("Which number's index ? : "))
print("occurance of",index)
for e in range(len(li)):
    if(li[e]==index):
        print(e)