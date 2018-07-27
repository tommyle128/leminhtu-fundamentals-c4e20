numb = int(input("Enter a number: "))

count = 0
loop = True

while numb != 0:
    numb = numb // 10
    count += 1

print(count)

    