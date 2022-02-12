a=[[1,2,3],[4,5,6]]
b=[]
k=1
i=0
while i<len(a): 
    j=0
    sum=0
    while j<len(a[i]):
       sum=a[i][j]+a[k][j]
       b.append(sum)
       j=j+1
    break 
print(b)
# 
a="SaRiKa"
b=""
i=0
while i<len(a):
    if a[i]>="A" and a[i]<="Z":
       b=b+a[i].lower()
    else:
        b=b+a[i].upper()
    i=i+1
print(b)
        
       