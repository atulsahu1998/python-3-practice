li = ['computer', 'science', 'student']
for e in range(len(li)):
    temp=''
    for i in range(len(li[e])):
        temp=temp+li[e][-(i+1)]
    li[e]=temp
print(li)