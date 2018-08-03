# quy = ["Quý", 20, "Vĩnh Phúc", 2, 3, ["Anime", "ping pong"]]
# dictionary
# CRUD
# key : value
person = {
    "name": "Quý",
    "age": 20,
    "university": "hust",
    "ex": 2,
    "favs": ["Anime", "ping pong"]
}

# delete
del person["age"]
print(person)del person["age"]
print(person)

# update
# person["ex"] = 20
# print(person)

# create
# person["gender"] = "male"
# print(person)

# read
# for key in person.keys():
#     print(key, end ="\t")

# for key, value in person.items():
#     print(key, value)

# for value in person.values():
#     print(value)

# key ="favs"
# if key in person:
#     print(person[key])
# else:
#     print("Not found")

