from random import choice
text = ["champion", "dungeon", "test"]
new_text = choice(text)
origin_list = list(new_text)
mix_list = []

loop = True
while loop:
    new_char = choice(origin_list)
    mix_list.append(new_char)
    origin_list.remove(new_char)
    if len(origin_list) == 0:
        loop = False
print(*mix_list, sep =", ")

ans = input("Enter your guess:")
if ans == new_text:
    print("Hura")
else:
    print("You failed")
   
  




    
    
    