import math
import argparse


# Creating a function calculating nominal interest rate (i)

def nominal_interest_rate(interest):
    i = interest / (12 * 100)
    return i


# Creating the function for calculating the number of payments
def calculate_payments_number(p, a, interest):
    i = nominal_interest_rate(interest)
    n = math.log(a / (a - i * p), 1 + i)
    total = math.ceil(n)
    years = total // 12
    months = total % 12
    overpay = total * a - p
    if years > 1:
        if months > 1:
            print(f"It will take {years} years and {months} months to repay this loan!")
        elif months == 1:
            print(f"It will take {years} years and {months} month to repay this loan!")
        elif months <= 0:
            print(f"It will take {years} years to repay this loan!")
    elif years < 1:
        if months > 1:
            print(f"It will take {months} months to repay this loan!")
        elif months == 1:
            print("It will take 1 month to repay this loan!")
    elif years == 1:
        if months > 1:
            print(f"It will take 1 year and {months} months to repay this loan!")
        elif months == 1:
            print(f"It will take 1 year and {months} month to repay this loan!")
        elif months < 1:
            print("It will take 1 year to repay this loan!")
    print(f"Overpayment = {overpay}")


# Creating function for calculating annuity payment:
def calculate_annuity(p, n, interest):
    i = nominal_interest_rate(interest)
    a = math.ceil(p * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
    overpay = a * n - p
    print(f"Your monthly payment = {a}!")
    print(f"Overpayment = {overpay}")


# Creating function for calculating loan principal:
def calculate_principal(a, n, interest):
    i = nominal_interest_rate(interest)
    p = math.floor(a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
    overpay = a * n - p
    print(f"Your loan principal = {p}!")
    print(f"Overpayment = {overpay}")


# Creating a function for differential calculation:

def calculate_differentiated(p, n, interest):
    i = nominal_interest_rate(interest)
    total = 0
    for j in range(1, n + 1):
        d = math.ceil(p / n + i * p * (1 - (j - 1) / n))
        total += d
        print(f'Month {j}: payment is {d}')
    overpay = total - p
    print(f'Overpayment = {overpay}')


# Initialization
parser = argparse.ArgumentParser(description="Loan calculator made with JetBrains")

# Creating the script arguments
parser.add_argument('--type', help="Loan payment type, Differential of Annuity")
parser.add_argument('--payment', help="Monthly Payment amount", type=int)
parser.add_argument('--principal', help="Credit principal", type=int)
parser.add_argument('--periods', help="The number of desired periods to repay the loan", type=int)
parser.add_argument('--interest', help="The loan interest rate", type=float)

# Arguments parser:

args = parser.parse_args()

# Error catcher:
if args.type not in ['annuity', 'diff']:
    print("Incorrect parameters!")
elif args.payment is not None and args.payment < 0 and args.principal is not None and args.principal < 0 and args.periods\
        is not None and args.periods < 0 and args.interest is not None and args.interest < 0:
    print("Incorrect parameters!")

# Main app flow:

if args.type == "annuity" and args.payment is not None and args.principal is not None and args.interest is not None \
        and args.periods is None:
    calculate_payments_number(args.principal, args.payment, args.interest)
elif args.type == "annuity" and args.payment is None and args.principal is not None and args.periods is not None \
        and args.interest is not None:
    calculate_annuity(args.principal, args.periods, args.interest)
elif args.type == "annuity" and args.payment is not None and args.principal is None and args.periods is not None \
        and args.interest is not None:
    calculate_principal(args.payment, args.periods, args.interest)
elif args.type == "diff" and args.payment is None and args.principal is not None and args.periods is not None and \
        args.interest is not None:
    calculate_differentiated(args.principal, args.periods, args.interest)
else:
    print("Incorrect parameters!")
