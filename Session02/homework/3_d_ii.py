n = int(input("Enter a number: "))

while n < 1:
    print("Please enter a positive number starting from 1")
    n = int(input("Enter a number: "))

else:
    for i in range (1, n+1):
        if i % 2 == 1:
            for j in range (1, n+1):
                if j % 2 == 1:
                    a = 1
                else:
                    a = 0
                print(a, end="\t")
            print()

            
        else:
            for j in range (1, n+1):
                if j % 2 == 1:
                    a = 0
                else:
                    a = 1
                print(a, end="\t")
            print()