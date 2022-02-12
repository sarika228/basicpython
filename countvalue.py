a={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
b={}
for x in a.keys():
    for y in a.values():
        c=0
        if c==2:
            if a[x]==y:
                a[y]=b[y]
            c=c+1
    print(b)