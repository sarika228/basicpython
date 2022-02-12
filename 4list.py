import json
a=['neelam','programer','24','2400']
b=['komal','trainer','24','20000']
c=['anuradha','HR','25','40000']
d=['Abhishek','manager','29','63000']  
x=['name','designation','age','salary']
e={}
f={}
g={}
h={}
y={}
i=0
while i<len(a):
    j=0
    while j<len(a):
        e[x[i]]=a[j]
        f[x[i]]=b[j]
        g[x[i]]=c[j]
        h[x[i]]=d[j] 
        j=j+1
        i=i+1
    y["emp1"]=e
    y["emp2"]=f
    y["emp3"]=g
    y["emp4"]=h    
print(json.dumps(y,indent=4))