"""
Name: Jeremy Miller
interest.py

Problem: This program calculates the monthly interest charge on a credit card account

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    annual_rate = eval(input("Enter the annual interest rate: "))
    billing_cycle = eval(input("Enter the number of days on the billing cycle: "))
    previous_balance = eval(input("Enter the previous net balance: "))
    payment = eval(input("Enter the payment amount: "))
    payment_day = eval(input("Enter the day of the billing cycle in which the payment was made: "))
    print()  # Prints new line

    # This converts the payment_day input into the number of days BEFORE the billing cycle ends
    # Ex. 31 days on the billing cycle, payment was made on day 20, then 31 - 20 = 11 days left
    days_left = billing_cycle - payment_day

    step_1 = previous_balance * billing_cycle
    step_2 = payment * days_left
    step_3 = step_1 - step_2
    step_4 = step_3 / billing_cycle

    monthly_rate = annual_rate / 12 * .01
    monthly_charge = step_4 * monthly_rate
    print(round(monthly_charge, 2))


if __name__ == '__main__':
    main()
