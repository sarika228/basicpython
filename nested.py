a=[1,2,3,4]
x=b={}
i=0
while i<len(a):
    b[a[i]]={}
    b=b[a[i]]
    i=i+1
print(x)
    