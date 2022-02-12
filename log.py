a=[1,0,0,1,1,0,1,1]
i=-1
j=0
sum=0
while i>=(-len(a)):
    b=a[i]*2**j
    sum=sum+b
    j=j+1
    i=i-1
print(sum)

# 
# print("Enter the Binary Number: ")
# bnum = int(input())

# dnum = 0
# i = 1
# while bnum!=0:
#     rem = bnum%10
#     dnum = dnum + (rem*i)
#     i = i*2
#     bnum = int(bnum/10)

# print("\nEquivalent Decimal Value = ", dnum)