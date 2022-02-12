pos=int(input("enter a pos:"))
i=1
count=0
while pos>=0:
    j=1
    c=0
    while j<i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        if count==pos:
            print(i)
            break
        count=count+1
    i=i+1