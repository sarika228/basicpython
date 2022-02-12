# i=5
# while i<=20:
#     j=0
#     while j<=4:
#         print(i-j,end="")
#         j=j+1
#     print()
#     i=i+5
    
# next patt
n="my name is sarika"
b=[]
i=0
m=input("enter the element:")
while i<len(n):
    c=""
    while True:
        if n[i]==m:
            b.append(c)
            b=b+[n[i]]
            i=i+1
            break
        else:
            c=c+n[i]
            i=i+1
        if i==len(n):
            b.append(c)
            break
print(b)
