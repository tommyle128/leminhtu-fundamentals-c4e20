numb = int(input ("Enter a number: "))

is_prime = True
divide = 2

while divide < numb:
    if numb % divide == 0:
        is_prime = False
    divide += 1

if is_prime and numb != 1:
    print(numb, "is a prime number")
else:
    print(numb, "is not prime number")




