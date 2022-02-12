a=['one','two','three','four','five']
b=[1,2,3,4,5,]  
i=0
d={}
while i<len(a):
    d.update({a[i]:b[i]})
    i=i+1
print(d)

# concatinating two lists into dictionary
a = ['a', 'b', 'c']
b= [1,2,3]
d = {}
c = 0
for i in a:
    d[i] = b[c]
    c += 1
print(d)

# method:-2
a=['a','b','c']
b=[1,2,3]
c = {}
for i in a:
    for j in b:
        c[i] = j
        b.remove(j)
        break  
print(c)
