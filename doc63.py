a=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
d=[]
b={}
i=0
while i<len(a):
    j=0
    index=0
    l=[]
    while j<len(a[i]):
        if a[i][j]==a[i][0]:
            pass
        else:
            l.append(a[i][j])
        j=j+1
    b[a[i][0]]=l
    i=i+1
print(b)

# 
a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d={}
key=[]
for i in a:
    if i[0] not in key:
        key.append(i[0])
for k in key:
    b=[]
    for j in a:
        if j[0]==k:
            b.append(j[1])
    d[k]=b
print(d)
        
    