a=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
b=[1, 2, 2, 3]
d={}
i=0
while i<len(a):
    d[a[i]]={b[i]}
    i=i+1
print(d)