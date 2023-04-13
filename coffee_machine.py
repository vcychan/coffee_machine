MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

while True:
    prompt = input("\nWhat would you like? (espresso/latte/cappuccino):\n")
    if prompt == 'off':
        break
    elif prompt == 'report':       
        for k, v in resources.items():
            print(f"{k.title()}: {v}")
        print(f"Money: ${profit}")
    
    if prompt == 'espresso':        
        if MENU['espresso']['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water.")
        elif MENU['espresso']['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))     
            x = float((quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01)) 
            if x == MENU['espresso']['cost']:
                print('Thank you, one espresso coming up!')
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                profit += 1.5                
            elif x > MENU['espresso']['cost']:
                change = (x) - (MENU['espresso']['cost'])
                round_change = round(change,2)
                print(f'Thank you, here is ${round_change} in change.')
                print("Enjoy your coffee!")
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                profit += 1.5                
            else:
                print("Sorry that's not enough money. Money refunded.")
        
    if prompt == 'latte':
        if MENU['latte']['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water.")
        elif MENU['latte']['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))     
            x = float((quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01))      
            if x == MENU['latte']['cost']:
                print('Thank you, one latte coming up!')
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['milk'] -= MENU['latte']['ingredients']['milk']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                profit += 2.0
            elif x > MENU['latte']['cost']:
                change = (x) - (MENU['latte']['cost'])
                round_change = round(change,2)
                print(f'Thank you, here is ${round_change} in change.')
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['milk'] -= MENU['latte']['ingredients']['milk']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                profit += 2.0
            else:
                print("Sorry that's not enough money. Money refunded.")
        
    if prompt == 'cappuccino':
        if MENU['cappuccino']['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water.")
        elif MENU['cappuccino']['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))     
            x = float((quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01))
            if x == MENU['cappuccino']['cost']:
                print('Thank you, one cappuccino coming up!')
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                profit += 3.0  
            elif x > MENU['cappuccino']['cost']:
                change = (x) - (MENU['cappuccino']['cost'])
                round_change = round(change,2)
                print(f'Thank you, here is ${change} in change.')
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                profit += 3.0 
            else:
                print("Sorry that's not enough money. Money refunded.")