stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    print('Inventory:') # your code goes here

    for key, value in inventory.items(): #for loop to go through each key/value
        print(value, key) #print in reverse order

    print('Total number of items:',sum(inventory.values()))

displayInventory(stuff)

   




