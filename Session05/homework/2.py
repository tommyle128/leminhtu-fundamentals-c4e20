numbers = [1, 6, 8, 1, 2, 1, 5, 6]
print(numbers)

ans = int(input("Enter a number? "))

# Cach 1: su dung count()
print()
print("Cach 1: su dung count()")
total_times = numbers.count(ans)
print(ans, "appear(s)", total_times,"times in my list")


# Cach 2: khong su dung count()
print()
print("Cach 2: khong su dung count()")
numb_dict = {}

for i in range (len(numbers)):
    numb_dict[str(numbers[i])] = 0
    for j in range (len(numbers)):
        if str(numbers[j]) == str(numbers[i]):
            numb_dict[str(numbers[i])] += 1

print(ans, "appear(s)", numb_dict[str(ans)],"times in my list")


        








