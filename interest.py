def main():

    principle = float(input('Enter the initial savings balance: ')) #Prompts user to input the initial savings account balance

    rate = 0.06 #The annual interest rate of the account
    n_yearly = 12 #Times per year the interest is compounded (monthly would be 12 times per year)

    month_1 = principle * (1.0 + (rate / n_yearly)) ** 1 #Calculates the balance after 1 month using compound interest formula
    month_2 = principle * (1.0 + (rate / n_yearly)) ** 2 #Calculates the balance after 2 months using compound interest formula
    month_3 = principle * (1.0 + (rate / n_yearly)) ** 3 #Calculates the balance after 3 months using compound interest formula

    print('Initial Balance: ', principle) #Prints the initial balance
    print('After One Month: ', month_1) #Prints the balance after one month
    print('After Two Months: ', month_2) #Prints the balance after two months
    print('After Three Months: ', month_3) #Prints the balance after three months

main()