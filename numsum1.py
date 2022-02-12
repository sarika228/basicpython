dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
for i,j in dic1.items():
    for x,y in dic2.items():
        if i==x:
            dic4[i]=(j+y)
            print(dic4)
        dic4.update(dic1)
        dic4.update(dic2)
        dic4.update(dic3)



#adding two dictionaries
# a={'a': 100, 'b': 200, 'c':300}
# b={'a': 300, 'b': 200, 'd':400}
# for i in a:
#     if i in b:
#         b[i]=a[i]+b[i]
#     else:
#         b[i]=a[i]
# print(b)