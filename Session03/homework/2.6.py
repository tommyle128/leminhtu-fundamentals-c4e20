flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and there are my sheep sizes:")
print(flock)

print()
highest = max(flock)
print("Now my biggest sheep has size:", highest,". Let's shear it!")
for index, item in enumerate(flock):
    if item == highest:
        flock[index] = 8
        print("After shearing, here is my flock:")
        print(flock)
print()

n = 4
for j in range (n-1):
    print("MONTH", j+1, ":")
    if j <2:
        for index2 in range (len(flock)):
            flock[index2] += 50
        print("One month has passed, now here is my flock:")
        print(flock)

        highest = max(flock)
        print("Now my biggest sheep has size:", highest,". Let's shear it!")

        for index, item in enumerate(flock):
            if item == highest:
                flock[index] = 8
                print("After shearing, here is my flock:")
                print(flock)
    else:
        for index2 in range (len(flock)):
            flock[index2] += 50
        print("One month has passed, now here is my flock:")
        print(flock)
        
        size_sum = 0
        for k in range (len(flock)):
            size_sum += flock[k]
        print("My flock has size in total: ", size_sum)
        print("I would get",size_sum," * $2 =","$",size_sum*2)
        
    print()

