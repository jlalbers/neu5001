'''
Jameson Albers
CS 5001
Spring 2021
Module 2 Practice 1

Calculates accrued compound monthly interest after 1, 2, and 3 months.
'''
# Use round function to shorten output

def main():

    # Prompts user to input the initial savings account balance
    principle = float(input('Enter the initial savings balance: '))

    rate = 0.06  # The annual interest rate of the account
    n_yearly = 12  # Compound frequency (monthly would be 12)

    # Use compount interest formula to calculate monthly balances
    month_1 = principle * (1.0 + (rate / n_yearly)) ** 1
    month_2 = principle * (1.0 + (rate / n_yearly)) ** 2
    month_3 = principle * (1.0 + (rate / n_yearly)) ** 3

    # Print the balances
    print('Initial Balance: ', principle)
    print('After One Month: ', round(month_1, 2))
    print('After Two Months: ', round(month_2, 2))
    print('After Three Months: ', round(month_3, 2))


main()
