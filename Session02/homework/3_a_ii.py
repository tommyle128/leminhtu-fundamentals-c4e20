n = int(input("Enter a number: "))

while n < 1:
    print("Please enter a positive number starting from 1")
    n = int(input("Enter a number: "))
else:
    for i in range (n):
        print(i, end=" ")