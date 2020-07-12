li1,even_sum,odd_sum,e= [1,12,123,234,345,456,567,678,789,890],0,0,0
while(e<len(li1)):
    if(li1[e]%2==0):even_sum+=li1[e]
    else:odd_sum+=li1[e]
    e+=1
print("Sum of Even numbrs : ",even_sum,"\n","Sum of odd numbers : ",odd_sum)

    
