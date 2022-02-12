import json
f=open("text.txt","r")
a={}
for i in f:
    s=i.split()
    if len(s)<2:
        a[s[0]]=s[1]
    else:
        j=1
        k=" "
        while j<len(s):
            k=k+s[j]
            j=j+1
            k=k+" "
        a[s[0]]=k
f1=open("text.json","w")
a=json.dump(a,f1)
