dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
fantasyInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}

def displayInventory(inventory):
    print('Inventory:')
    count = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        count += v
    print('Total number of items: ' + str(count))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

displayInventory(fantasyInventory)
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
