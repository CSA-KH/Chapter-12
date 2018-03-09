#Keenan H
#2-28-18
#comp prog

def inventory_():
    inventory = {'Banana': 100, 'Blackberries': 100, 'Orange': 100, 'cat': 10}
    ch = input('What item do you need to change? ')
    r = int(input('How many do you want to remove? '))
    print('You now have %s %s(s)' %(inventory[ch]-r, ch))

inventory_()
