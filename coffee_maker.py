water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550

balance = [water, milk, coffee_beans, cups, money]

while True:

    action = input('Write action (buy, fill, take, remaining, exit):\n')
    if action == 'exit':
        break

    def back_action():
        print()
        return action


    def print_balance():
        global balance
        print('The coffee machine has: ')
        print(f'{balance[0]} of water')
        print(f'{balance[1]} of milk')
        print(f'{balance[2]} of coffee beans')
        print(f'{balance[3]} of disposable cups')
        print(f'${balance[4]} of money\n')


    def convert_volumes():
        global balance
        for el in balance:
            if el:
                position = balance.index(el)
                if position == 0:
                    return 'water'
                if position == 1:
                    return 'milk'
                if position == 2:
                    return 'coffee_beans'
                if position == 3:
                    return 'cups'
                if position == 3:
                    return 'money'


    def check_balance():
        global balance
        if all([el > 0 for el in balance]):
            print('I have enough resources, making you a coffee!\n')
        for el in balance:
            if el < 0:
                print(f'Sorry, not enough {convert_volumes()}!\n')


    def espresso():
        global balance
        balance = [balance[0] - 250, balance[1], balance[2] - 16, balance[3] - 1, balance[4] + 4]
        return balance


    def latte():
        global balance
        balance = [balance[0] - 350, balance[1] - 75, balance[2] - 20, balance[3] - 1, balance[4] + 7]
        return balance


    def cappuccino():
        global balance
        balance = [balance[0] - 200, balance[1] - 100, balance[2] - 12, balance[3] - 1, balance[4] + 6]
        return balance


    def back_espresso():
        global balance
        balance = [balance[0] + 250, balance[1], balance[2] + 16, balance[3] + 1, balance[4] - 4]
        return balance


    def back_latte():
        global balance
        balance = [balance[0] + 350, balance[1] + 75, balance[2] + 20, balance[3] + 1, balance[4] - 7]
        return balance


    def back_cappuccino():
        global balance
        balance = [balance[0] + 200, balance[1] + 100, balance[2] + 12, balance[3] + 1, balance[4] - 6]
        return balance

    #  Начну с ф-й, которые выполняют каждое действие
    def buy():
        global balance
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        enter = input()
        if enter == '1':
            espresso()
            check_balance()
            for el in balance:
                if el < 0:
                    back_espresso()
        elif enter == '2':
            latte()
            check_balance()
            for el in balance:
                if el < 0:
                    back_latte()
        elif enter == '3':
            cappuccino()
            check_balance()
            for el in balance:
                if el < 0:
                    back_cappuccino()
        elif enter == 'back':
            back_action()

    def fill():
        global balance
        water_input = int(input('Write how many ml of water do you want to add:\n'))
        milk_input = int(input('Write how many ml of milk do you want to add:\n'))
        coffee_beans_input = int(input('Write how many grams of coffee beans do you want to add:\n'))
        cups_input = int(input('Write how many disposable cups of coffee do you want to add:\n'))
        print()
        balance = [balance[0] + water_input, balance[1] + milk_input, balance[2] +
                   coffee_beans_input, balance[3] + cups_input, balance[4]]
        return balance


    def take():
        global balance
        cash = balance[4]
        print(f'I gave you {cash}')
        print()
        balance = [balance[0], balance[1], balance[2], balance[3], balance[4] - cash]
        return balance


    def remaining():
        return print_balance()


    def choose_action():
        global action
        if action == 'buy':
            print()
            buy()
        elif action == 'fill':
            print()
            fill()
        elif action == 'take':
            print()
            take()
        elif action == 'remaining':
            print()
            print_balance()
        elif action == 'exit':
            print()


    choose_action()
