yob = int(input("What's your birth year?"))
import datetime
yearnow = int(datetime.datetime.now().year)
age = yearnow - yob
print(age)


