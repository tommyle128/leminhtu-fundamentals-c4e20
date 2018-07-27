fav = ["death note", "netflix", "teaching"]
print("Hi there, here your favorite things so far")
print(*fav, sep=", ")

them = input("Name one thing you wwant to add?")
fav.append(them)
print(*fav, sep=", ")