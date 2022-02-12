# a={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# c=0
# for i in a.values():
#     j=0
#     while j<len(i):
#         c=c+1
#         j=j+1
# print(c)

# 
a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
d={}
b=[]
for i,j in a.items():
    for k in j:
        d[i]=k
b.append(d)
print(b)

# print(b)
# j=0
# c=[]
# while j<len(b):
#     k=0
#     while k<len(b[j]):
#         c.append(b[j][k])
#         k=k+1
#     j=j+1
# print(c)

    