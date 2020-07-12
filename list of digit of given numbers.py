li1,li2 = [1,12,123,234,345,456,567,678,789,890],[]
for e in range(len(li1)):
    li2.append(li1[e]%10)
print(li2)