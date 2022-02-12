a = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
# max=0
# for i in a:
#     c=0
#     for j in a:
#         if a[i]>a[j]:
#             max=a[i]
#             c=c+1
#         if c==3:
#             print(max)
#             break
        
max=0
for i in a:
    c=0
    for j in a:
        if a[i]>a[j]:
            max=i
            c=c+1
        if c==3:
            print(max)
            break
        