print("Guess my number game")
print("Think of a number from 0 to 100. Then Press 'Enter'")
input()

low = 0
high = 100
loop = True

print("""
All you have to do is to answer my guess
'c' if my guess is 'C'orrect!
's' if my guess is 's'maller than your number!
'l' if my guess is 'L'arger than your number!
""")

while loop:
    mid = (low + high) // 2
    ans = input(("Is {} your number?").format(mid))
    if ans == "c":
        print("I knew it!")
        break
    elif ans == "s":
        low = mid
    elif ans == "l":
        high = mid
    
 

    



