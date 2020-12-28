import sqlite3
import random

list_of_data = []


# Создаю БД card.s3db
database_sql = sqlite3.connect('card.s3db')
sql_request = database_sql.cursor()

sql_request.execute("CREATE TABLE IF NOT EXISTS card(id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")
database_sql.commit()


def luhn(number):
    list_card = [int(el) for el in number]
    odd_list = [el * 2 if i % 2 == 0 else el for i, el in enumerate(list_card)]
    subtract_list = [el - 9 if el > 9 else el for el in odd_list]
    check_sum = sum(subtract_list) * 9 % 10
    list_card.append(check_sum)
    card_client = [str(num) for num in list_card]
    card_client = ''.join(card_client)
    return card_client


while True:
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')

    choose_option = int(input())

    if choose_option == 1:
        card = '400000' + str(random.randint(100000000, 900000000))
        pin = str(random.randint(1000, 9000))
        list_of_data = [luhn(card), pin]
        values = f'INSERT INTO card ("number", "pin") VALUES ({list_of_data[0]}, {list_of_data[1]})'
        sql_request.execute(values)
        database_sql.commit()

        print()
        print('Your card has been created')
        print('Your card number:')
        print(list_of_data[0])
        print('Your card PIN:')
        print(list_of_data[1])
        print()

    if choose_option == 2:
        get_data = sql_request.execute('SELECT * FROM card').fetchall()
        list_of_numbers = [number[1] for number in get_data]
        list_of_pins = [pin[2] for pin in get_data]

        print()
        print('Enter your card number:')
        enter_card = input()
        print('Enter your PIN:')
        enter_pin = input()
        if enter_card not in list_of_numbers or enter_pin not in list_of_pins:
            print()
            print('Wrong card number or PIN!')
            print()
        else:
            print()
            print('You have successfully logged in!')
            print()
            while True:
                print('1. Balance')
                print('2. Add income')
                print('3. Do transfer')
                print('4. Close account')
                print('5. Log out')
                print('0. Exit')
                option_of_card = int(input())

                get_data = sql_request.execute(f'SELECT * FROM card WHERE number = {enter_card}')
                balance = get_data.fetchone()

                if option_of_card == 1:
                    print()
                    print('Balance: ', balance[-1])
                    print()
                if option_of_card == 2:
                    print()
                    print('Enter income:')
                    amount_of_money = int(input())
                    update_data = f'UPDATE card SET balance = {balance[-1] + amount_of_money} ' \
                                  f'WHERE number = {enter_card}'
                    new_data = sql_request.execute(update_data)
                    database_sql.commit()
                    print('Income was added!')
                    print()

                if option_of_card == 3:
                    get_data = sql_request.execute('SELECT * FROM card').fetchall()
                    check_card = sql_request.execute(f'SELECT * FROM card WHERE number = {enter_card}')
                    get_check_card = int(check_card.fetchone()[1])
                    list_of_numbers = [number[1] for number in get_data]

                    print()
                    print('Transfer')
                    print('Enter card number: ')
                    transfer_card = input()
                    check_sum_luhn = transfer_card[:-1]
                    if transfer_card != luhn(check_sum_luhn):
                        print('Probably you made a mistake in the card number. Please try again!')
                        print()
                        continue
                    if transfer_card == luhn(check_sum_luhn) and int(transfer_card) == get_check_card:
                        print("You can't transfer money to the same account!")
                        print()
                        continue
                    if transfer_card == luhn(check_sum_luhn) and transfer_card not in list_of_numbers:
                        print('Such a card does not exist')
                        print()
                        continue
                    elif transfer_card == luhn(check_sum_luhn):
                        print('Enter how much money you want to transfer:')
                        money = int(input())

                        new_sql = f'SELECT * FROM card WHERE number = {enter_card}'
                        value = sql_request.execute(new_sql).fetchone()[-1]

                        if value - money < 0:
                            print('Not enough money!')
                            print()
                        else:
                            update_data = f'UPDATE card SET balance = {value - money} ' \
                                          f'WHERE number = {enter_card}'
                            new_data = sql_request.execute(update_data)
                            database_sql.commit()

                            transfer_money = f'UPDATE card SET balance = {+ money} WHERE number = {transfer_card}'
                            transfer_ok = sql_request.execute(transfer_money)
                            database_sql.commit()

                            print('Success!')
                            print()

                if option_of_card == 4:
                    delete_account = f'DELETE FROM card WHERE number = {enter_card}'
                    sql_request.execute(delete_account)
                    database_sql.commit()
                    list_of_data = []
                    print()
                    print('The account has been closed!')
                    print()
                    break

                if option_of_card == 5:
                    print()
                    print('You have successfully logged out!')
                    print()
                    break

                if option_of_card == 0:
                    break

            if option_of_card == 0:
                break

    if choose_option == 0:
        break
print()
print('Bye!')
