# a={"V":[1,4,6,10],"VI":[1,4,12],"VII":[1,3,8]}
# b=[]
# for i in a.values():
#    b.append(i)
# # print(b)
# j=0
# k=0
# c=[]
# while j<len(b)-1:
#     d=b[j]+b[j+1]
#     c.append(d)
#     j=j+1
# print(c)

# 
a=[1,2,3]
b=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append({a[i]})
    i=i+1
print(b)