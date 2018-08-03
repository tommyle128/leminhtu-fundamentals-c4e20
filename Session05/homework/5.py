price = {}
price["banana"] = 4
price["apple"] = 2
price["organge"] = 1.5
price["pear"] = 3

stock = {}
stock["banana"] = 6
stock["apple"] = 0
stock["organge"] = 32
stock["pear"] = 15


total = 0

for key, value in price.items():
    for key2, value2 in stock.items():
        if key == key2:
            print(key)
            print("Price:", value)
            print("Stock: ", value2)
            
            total_item = value * value2
            print("Total of this item: ", total_item)
            print()
            total = total + total_item

    
print("Total money you need: ", total)




