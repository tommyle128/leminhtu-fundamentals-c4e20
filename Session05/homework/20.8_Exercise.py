text = input("Enter a string:").lower()
text = text.replace(" ","")
char = list(text)
char = sorted(char, key =str.lower)

char_dict = {}

for i in range (len(char)):
    char_dict[char[i]] = 0
    for j in range (len(char)):
        if char[j] == char[i]:
            char_dict[char[i]] += 1

for key, value in char_dict.items():
    print(key," ", value, end ='\n')
