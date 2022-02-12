# a=[{"name":"sarika","age":22,"hobby":"singing"},{"name":"muskan","age":21,"hobby":"coding"}]
# n=input("enter the name:")
# i=0
# while i<len(a):
#     for key in a[i]:
#         if n==a[i][key]:
#             print(a[i])
#     i=i+1

# table format
a= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in a:
    print(i)
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j=j+1
#     b=a[i]
#     j=0
#     k=0
#     while j<len(b[k]):
#         print(b[j][k])
#         print(k)
#         k=k+1
#         j=j+3
        


# # C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11