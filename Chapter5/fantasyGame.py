def displayInventory(inventory):
    print('Inventory:')
    count = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        count += v
    print('Total number of items: ' + str(count))

fantasyInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(fantasyInventory)
