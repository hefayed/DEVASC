import yaml

with open("myfile.yml", "r") as file:
    # converting a YAML file to a python dictionary
    data = yaml.safe_load(file)
print(type(data))
user = data["user"]
print(user["name"])
for role in user["roles"]:
    print(role)
user["location"]["city"] = "Dallas"
with open("myfile.yml", "w") as file:
    #  saving a YAML file from a python dictionary
    yaml.dump(data, file, default_flow_style=False)
