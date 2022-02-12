a=[5,8,2,9,1,4]
i=0
j=len(a)-1
while j>i:
    a[i],a[j]=a[j],a[i]
    i=i+1
    j=j-1
print(a)
