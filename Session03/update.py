print("Hi there, here are your favorite things so far")
menu = ["death note", "netflix", "teaching"]

print("*" * 30)
for i, a in enumerate(menu):
        print("{}. {}".format(i + 1, a))
print("*" * 30)

pos = int(input("Position you want to update? "))
rep = input("Your replacing favorite? ")
menu[pos-1] = rep

print("*" * 30)
for j, a in enumerate(menu):
        print("{}. {}".format(j + 1, a))
print("*" * 30)


