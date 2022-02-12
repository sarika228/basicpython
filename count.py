a="MISSISSIPPI" 
i=0
c_M=0
c_I=0
c_S=0
c_P=0
letter=[]
num=[]
while i<len(a):
    if a[i]=="M":
        c_M+=1
        letter.append("M")
        num.append(c_M)
    elif a[i]=="I":
        c_I+=1
        letter.append("I")
        num.append(c_I)
    elif a[i]=="S":
        c_S+=1
        letter.append("S")
        num.append(c_S)
    elif a[i]=="P":
        c_P+=1
        letter.append("P")
        num.append(c_P)
    i=i+1
dictionary=dict(zip(letter,num))
print(dictionary)