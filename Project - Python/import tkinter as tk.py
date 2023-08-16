import tkinter as tk
from tkinter import messagebox

def display_balance():
    messagebox.showinfo("Balance", f"Your balance is £{balance:.2f}")

def deposit_money():
    global balance
    deposit_input = entry_amount.get()
    try:
        deposit_amount = float(deposit_input)
        balance += deposit_amount
        display_balance()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def withdraw_money():
    global balance
    withdraw_input = entry_amount.get()
    try:
        withdraw_amount = float(withdraw_input)
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            display_balance()
        else:
            messagebox.showerror("Error", "Insufficient balance.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def on_quit():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.destroy()

balance = 0

root = tk.Tk()
root.title("Banking Operations")

label_balance = tk.Label(root, text="Balance: £0.00")
label_balance.pack()

label_amount = tk.Label(root, text="Enter amount:")
label_amount.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

btn_display = tk.Button(root, text="Display Balance", command=display_balance)
btn_display.pack()

btn_deposit = tk.Button(root, text="Deposit Money", command=deposit_money)
btn_deposit.pack()

btn_withdraw = tk.Button(root, text="Withdraw Money", command=withdraw_money)
btn_withdraw.pack()

btn_quit = tk.Button(root, text="Quit", command=on_quit)
btn_quit.pack()

root.mainloop()
