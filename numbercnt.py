a={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
d={}
b=[]
for v in a.values():
    b.append(v)
i=0
while i<len(b):
    j=0
    c=0
    while j<len(b):
        if b[i]==b[j]:
            c=c+1
        j=j+1
    d.update({b[i]:c})
    i=i+1
print(d)




