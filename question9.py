import json
dict={
    "shopping_list":
        { 
            "chaco":15,
            "Biscuits":50,
            "Diary_milk":30,
            "ice_cream":20,
        } 
}
item=input("enter which item would you like to buy=")
no_of_item=int(input("PLEASE enter How many item would you like to buy="))
for key in dict:
    for i in dict[key]:
        if i == item:
            dict[key][i]=(dict[key][i]-no_of_item)
print(json.dumps(dict, indent=4))
# import json
# x={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20"}}
# y=json.dumps(x)
# n=input("enter item to buy:")
# n1=int(input("how many items u want:"))
# for i in y:
#     del i["chaco"] and i["Biscuits"]
#     for i in y:
#         z={"chaco":"15"} and {"Biscuits":"50"}
#         y.update(z)
# print(y)
