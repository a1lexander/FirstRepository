import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="Choose between annuity or diff")
parser.add_argument("--principal", type=int, help="the loan principal")
parser.add_argument("--periods", type=int, help="for number of monthly payments")
parser.add_argument("--interest", type=float, help="Enter the loan interest")
parser.add_argument("--payment", type=int, help="Enter the monthly payment amount")

args = parser.parse_args()

if args.type == 'diff' and args.payment is None and args.principal and args.interest and args.periods:
    if args.principal >= 0 and args.interest >= 0 and args.periods >= 0:
        P = args.principal
        i = float(args.interest) / 100 / 12
        n = args.periods
        m = 0
        all_periods = 0
        for m in range(n):
            m += 1
            D = P / n + i * (P - P * (m - 1) / n)
            D = math.ceil(D)
            print(f'Month {m}: payment is {D}')
            all_periods += D
        overpayment = P - all_periods
        print('Overpayment = ', abs(overpayment))
    else:
        print('Incorrect parameters')

elif args.type == 'annuity' and args.payment is None and args.principal and args.interest and args.periods:
    if args.principal >= 0 and args.interest >= 0 and args.periods >= 0:
        P = args.principal
        i = float(args.interest) / 100 / 12
        n = args.periods
        A = P * (i * pow((1 + i), n)) / (pow((1 + i), n) - 1)  # весь срок
        A = math.ceil(A)
        print(f'Your annuity payment = {A}!')
        print('Overpayment = ', abs(P - A * n))

elif args.type == 'annuity' and args.periods is None and args.principal and args.payment and args.interest:
    if args.principal >= 0 and args.payment >= 0 and args.interest >= 0:
        P = args.principal
        A = args.payment
        i = float(args.interest) / 100 / 12
        base = A / (A - i * P)
        n = math.log(base, 1 + i)
        n = math.ceil(n)
        year = n / 12
        month = round((year % 1) * 12)
        year = math.floor(year)
        print(f'It will take {year} years to repay this loan!')
        print('Overpayment = ', abs(P - A * n))

elif args.type == 'annuity' and args.payment and args.periods and args.interest:
    if args.payment >= 0 and args.periods >= 0 and args.interest >= 0:
        A = args.payment
        n = args.periods
        i = float(args.interest) / 100 / 12
        P = A / ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1))
        P = math.floor(P)
        print(f'Your loan principal = {P}!')
        print('Overpayment = ', abs(P - A * n))
else:
    print('Incorrect parameters')



