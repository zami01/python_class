# 
import json 


# reading json file from current directory
with open("data.json", "r") as data_file:
    data = json.load(data_file) 


print(data["class"])
print(data["instructors"])
