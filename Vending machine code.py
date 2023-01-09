items = [
    {
        'code':0,
        'name':'Mountain Dew',
        'price':2
    },
    {
        'code':1,
        'name':'Snickers',
        'price':3
    },
    {
        'code':2,
        'name':'Doritos',
        'price':1
    },
]

is_quit = False
item = ''

while is_quit == False:
    print("Hello! What would you like?")
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")

    query = int(input("Write the number of the item you want: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Good choice!, {item['name']} will cost you {item['price']} Dirhams.")

        price = int(input(f"Enter {item['price']} Dirhams to purchase: "))
        if price == item['price']:
            print(f"Thank you for buying items from this vending machine! Enjoy your {item['name']}")
        else:
            print(f"Please enter only {item['price']} Dirhams")

    query = input("If you want to stop, press q. If you would like to purchase anything else, press c. : ")
    if query == 'c':
        is_quit = False
    else:
        is_quit = True
    print('')