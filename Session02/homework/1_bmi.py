h = int(input("Insert your height(cm): ")) / 100
w = int(input("Insert your weight(kg): "))

bmi = w / (h ** 2)

print("Based on BMI:")
if bmi < 16:
    print("You are severly underweight!")
elif bmi <= 18.5:
    print("You are underweight!")
elif bmi <= 25:
    print("You are normal!")
elif bmi <= 30:
    print("You are overweight!")
else:
    print("You are obese!")




