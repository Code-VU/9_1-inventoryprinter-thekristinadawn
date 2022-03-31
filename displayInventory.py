stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
# your code goes here
    print('Inventory:')
    
    for key, value in stuff.items(): #for loop to go through each key/value
        print(value, key) #print in reverse order
    

displayInventory(stuff)
print('Total number of items:',sum(stuff.values()))


