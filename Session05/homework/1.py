inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print("Set value of 'pocket': ")
print(inventory)

inventory['backpack'].remove('dagger')
print("Remove 'dagger' from 'backpack': ")
print(inventory)

inventory['gold'] = [500, 50]
print("Add 50 to 'gold' key: ")
print(inventory)
