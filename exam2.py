# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     j=1
#     while j<=n:
#         print(i*j,end="")
#         j=j+1
#     print()
#     i=i+1

# a={"h":"red","s":"red","m":"black","g":"green","k":"green"}
# for i in a:
#     c=0
#     for j in a:
#         if a[i]==a[j]:
#             c=c+1
#     if c>1:
#         print(i)

n=int(input("enter the number:"))
i=n-7
while i<=n:
    if i%2==0:
        print(n)
    n=n+1
print("**************")
k=i
while k<i+5:
    if i%2!=0:
        print(n)
    n=n+1