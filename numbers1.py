#code for finding sum, max, min, average

li=[]
for i in range (0,5):
    a=int(input("enter the numbers: "))
    li.append(a)
print("sum is ",sum(li))
print("min is ",min(li))
print("max is ",max(li))
a=len(li)
avg=sum(li)/len(li)
print("avg is ",avg)


