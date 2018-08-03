teen_code = {
    "hc" : "học",
    "ng" : "người",
    "pt" : "phân tích",
    "eny": "em người yêu",
    "any": "anh người yêu",
    "ns": "nói",
    "ngta": "người ta",
    "lm": "làm",
    "r": "rồi",
    "stt": "status"
    
}

loop = True

while loop:
    print("*"*30)
    for key in teen_code.keys():
        print(key, end ="\t")
    print()
    ans = input("Code: ")
    if ans in teen_code:
        print("Translation: ", teen_code[ans])
        loop = False
          
    else:
        lua_chon = input("Not found, do you want to contribute this word (Y/N)").upper()
        if lua_chon == "Y":
            meaning = input("Your meaning: ")
            teen_code[ans] = meaning
            print("Updated")
            loop = False
        else:
            loop = False

print("*"*30)



