player = {'rope':1, 'torch':6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addtoInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory.setdefault(item, 1)

addtoInventory(player, dragonLoot)
displayInventory(player)
