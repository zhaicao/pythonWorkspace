
with open("docker-compose.yml") as myFile:
    print(myFile.read())


aList = []
aList.append("a")
aList.append("b")
aList.append("c")

print(aList)


hm = {
     "Mike": "sss-1111",
     "Lucy": "sss-2222",
     "Jack": "sss-3333"
}

for key, value in hm.items():
    print(key, value)

del hm["Mike"]
count = len(hm)
hm["Susan"] = (1,2,3,4)
print(hm.keys())
hm.clear()
