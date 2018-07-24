n = int(input("Enter a number: "))

while n < 0:
    print("Please enter a positive number starting from 0")
    n = int(input("Enter a number: "))
else:
    f = 1
    for i in range (1, n+1):
        f = f * i

print("The total factorial of", n, "is", f)
