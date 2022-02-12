n=int(input("enter the number:"))
m=n
i=1
c=0
while i<=n:
    if n%2==0:
        print(n)
        i=i+1
    if c==3:
        break
    n=n-1
print("--------------------------")
j=1
ct=0
while j<=m:
    if m%3==0:
        print(m)
        m=m+1
    if ct==3:
        break
    j=j+1