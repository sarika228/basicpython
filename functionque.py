def num(n):
    i=0
    sum=0
    while i<=n:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    return sum
n=int(input("enter the number:"))
print(num(n))