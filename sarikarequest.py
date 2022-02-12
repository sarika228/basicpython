import requests
import json
result=requests.get("http://saral.navgurukul.org/api/courses")
# print(result.text)
data=result.json()
# print(data)
with open("courses.json","w") as f:
    json.dump(data,f,indent=4)
    a=data["available_courses"]
    count=1
    for i in range(0,len(a)):
        id= a[i]["id"]
        name=a[i]["name"]
        count=count+1
    print(id,name,count)



