# list
# create
menu = ["Cơm", "Cá", "Thịt bò", "Ghẹ", "Pizza", "Tôm hùm"]
# separator
# print(*menu, sep=", ")
# menu.append("Ghẹ")
# print(*menu, sep=", ")
# # length
# print(len(menu))
# menu.append("Ghẹ")
# print(len(menu))
# for i in range (len(menu)):
#     print(menu[i])

# for index, item in enumerate(menu):
#     print("{}. {}".format(index + 1, item))
# for item in menu:
#     print(item)

# update
print(*menu, sep=", ")
menu[4]= "Gà"
print(*menu, sep=", ")