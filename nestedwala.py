# a=['S001', 'S002', 'S003', 'S004']
# b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# c=[85, 98, 89, 92]
# dict2={}
# list=[]
# i=0
# while i<len(b):
#     dict1={}
#     dict1[b[i]]=c[i]
#     dict2[a[i]]=dict1
#     i=i+1
# list.append(dict2)
# print(list)

a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
b=[]
for i in a.values():
   b.append(i)
b1=[]
i=0
while i<4:
    j=0
    d={}
    for k in a:
        d[k]=b[j][i]
        j+=1
    b1.append(d)
    i=i+1
print(b1)
    # print(dict)

# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
