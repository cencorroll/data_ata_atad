import sys

def display_balance(current_balance):
    print(f'Your balance is £{current_balance:.2f}')

def deposit_money(current_balance):
    deposit_input = input('Please choose an amount to deposit: ')
    deposit_amount = int(deposit_input)
    current_balance += deposit_amount
    print(f'Your new balance is £{current_balance:.2f}')
    return current_balance

def withdraw_money(current_balance):
    withdraw_input = input('''
                           Please choose an amount to withdraw: 
                           1. £10
                           2. £20
                           3. £40
                           4. £60
                           5. Other Amount
                           ''')
    withdraw_choice = int(withdraw_input)
    if withdraw_choice == 1:
        current_balance -= 10
    elif withdraw_choice == 2:
        current_balance -= 20
    elif withdraw_choice == 3:
        current_balance -= 40
    elif withdraw_choice == 4:
        current_balance -= 60
    elif withdraw_choice == 5:
        other_input = input('Please specify the amount to withdraw in multiples of 10: ')
        other_amount = int(other_input)
        if other_amount % 10 == 0:
            current_balance -= other_amount
        else:
            print('This is not a valid amount. Please choose again')
    else:
        print('Invalid choice. Please select a valid option.')

    print(f'Your new balance is £{current_balance:.2f}')
    return current_balance

balance = 0
pin = 1234

pin_input = int(input('Please enter your pin: '))
if pin_input != pin:
    print('Pin is incorrect. Goodbye')
    sys.exit()

while True:
        user_input = input('''
                           1. Display Balance
                           2. Deposit Money
                           3. Withdraw Money
                           4. Return Bank Card
                           Choose an option ''')

        choice = int(user_input)

        if choice == 4:
            print('Here is your card. Goodbye')
            sys.exit()

        if choice == 1:
            display_balance(balance)
        elif choice == 2:
            balance = deposit_money(balance)
        elif choice == 3:
            balance = withdraw_money(balance)
        else:
            print('Invalid choice. Please select a valid option.')



