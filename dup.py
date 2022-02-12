a={'ball':'red','bat':4,'wickets':8,'ball':'green','bat':3} 
b={}
for i in a:
    if a[i] not in b:
        b[i]=a[i]
print(b)