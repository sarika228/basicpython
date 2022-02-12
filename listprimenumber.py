a=[1,5,6,10,15,11,13]
i=0
while i<len(a):
    j=a[i]
    k=1
    c=0
    while k<j:
        if j%k==0:
            c+=1
        k+=1
    if c==1:
        print(a[i],"prime")
    i+=1

# exam
a=["my","name","is","sarika"]
b=""
i=0
while i<len(a):
    b=b+" "+a[i]
    i=i+1
print(b)