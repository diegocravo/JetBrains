import argparse
from math import ceil, log, floor

# parser
parser = argparse.ArgumentParser()
# arguments
parser.add_argument('--type')
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)

args = parser.parse_args()

def diff():
    global month_values
    month_values = []
    for x in range(count_of_periods):
        month_values.append(ceil((args.principal / count_of_periods) + (nominal_interest() * (args.principal - ((args.principal*((x+1) - 1)) / count_of_periods)))))

def nominal_interest(): #i
    return credit_interest / (12 * 1)

def count_periods(): #n
    return ceil(log((monthly_payment / (monthly_payment - nominal_interest() * credit_principal)), 1 + nominal_interest()))

def years_months():
    if count_periods() % 12 == 0:
        return (f'You need {floor(count_periods() / 12)} years to repay this credit!')
    elif count_periods() < 12:
        return (f'You need {floor(count_periods())} months to repay this credit!')
    elif count_periods() % 12 != 0:
        return (f'You need {floor(count_periods() / 12)} years and {count_periods() % 12} months to repay this credit!')

def annuity(): #A
    return ceil(credit_principal * (  (nominal_interest()*(pow(1+nominal_interest(), count_of_periods))) / ((pow(1+nominal_interest(), count_of_periods))  - 1)))

def credit(): #P
    return floor(monthly_payment / (  (nominal_interest()*(pow(1+nominal_interest(), count_of_periods))) / ((pow(1+nominal_interest(), count_of_periods))  - 1)))

def overpayment(): # overpayment annuity
    return round((annuity() * args.periods) - args.principal)

def overpayment_periods(): # Overpayment for annuity monthly payment
    return round((args.payment * count_periods()) - args.principal)

def overpayment_credit_principal(): # Overpayment for credit principal
    return round((args.payment * args.periods) - credit())

def overpayment_diff(): #overpayment diff
    return sum(month_values) - args.principal

def check_args_interest():
    if args.interest != None:
        return True
    else:
        return False

credit_principal = None
count_of_periods = None
credit_interest = None
monthly_payment = None

if args.type == 'diff':
    credit_principal = args.principal
    count_of_periods = args.periods
    if check_args_interest():
        credit_interest = args.interest / 100
        diff()
        for y in range(count_of_periods):
            print(f'Month {y + 1}: paid out {month_values[y]}')
        print(f'\nOverpayment = {overpayment_diff()}')
    else:
        print('Incorrect parameters')
# 3 possible outputs
elif args.type == 'annuity':
    credit_principal = args.principal
    count_of_periods = args.periods
    monthly_payment = args.payment
    if check_args_interest():
        credit_interest = args.interest / 100
    # annuity
    if monthly_payment == None:
        if credit_principal == None or count_of_periods == None or credit_interest == None:
            print('Incorrect parameters')
        else:
            print(f'Your annuity payment = {annuity()}!')
            print(f'Overpayment = {overpayment()}')
    # count of months
    elif count_of_periods == None:
        if credit_principal == None or monthly_payment == None or credit_interest == None:
            print('Incorrect parameters')
        else:
            print(years_months())
            print(f'Overpayment = {overpayment_periods()}')
    # credit principal
    elif credit_principal == None:
        if  count_of_periods == None or monthly_payment == None or credit_interest == None:
            print('Incorrect parameters')
        else:
            print(f'Your credit principal = {credit()}!')
            print(f'Overpayment = {overpayment_credit_principal()}')
else:
    print('Incorrect parameters')