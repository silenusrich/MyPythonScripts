def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    itemNum = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print('\n' + 'Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    # your code goes here
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)
        inventory[addedItems[i]] = inventory[addedItems[i]] + 1
    return inventory        

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
