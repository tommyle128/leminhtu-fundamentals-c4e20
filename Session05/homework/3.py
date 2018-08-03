numb = int(input("How many bacteria are there? "))
time = int(input("How much time in minutes will we wait? "))

final_bact = numb
for i in range (int(time/2)):
    final_bact = final_bact * 2

print("After", time, "minute(s)", "we would have", final_bact, "bacteria(s)")