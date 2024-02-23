def add_to_inventory(inventory, additems):
    for k in range(len(additems)):
        if additems[k] in inventory.keys():
            inventory[additems[k]] += 1
        else:
            inventory.setdefault(additems[k], 1)
    return inventory


def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

inv = {'rope': 1, 'gold coin': 42}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
