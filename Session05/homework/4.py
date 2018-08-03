months = 4
pair = 1

rabbit = {}

for i in range (months+1):
    if i == 0:
        rabbit[str(i)] = pair
    elif i == 1:
        rabbit[str(i)] = pair + 1
    else:
        rabbit[str(i)] = rabbit[str(i-1)] + rabbit[str(i-2)]
        
       
for key, value in rabbit.items():
    print("Month", key,": ", value, "pair(s) of rabbit")
    
