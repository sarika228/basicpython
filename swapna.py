a=[1,3,9,5,7]
b=[2]
c=a+b
c.sort()
print(c)
if len(c)%2!=0:
    median=(len(c)/2)-0.5
    print(c[int(median)])
else:
    value=int(len(c)/2)
    median2=(c[value]+c[value-1])/2
    print(median2)
    
