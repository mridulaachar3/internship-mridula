# Simple Payment Application

import datetime
import random
import math

# custom exceptions
class WrongPINError(Exception):
    pass

class LowBalanceError(Exception):
    pass

class BadAmountError(Exception):
    pass


# ---- setup ----
correct_pin = "1234"
wallet_balance = 0


# functions 

def get_txn_id():
    # generates a random transaction id using random module
    num = random.randint(100000, 999999)
    return "TXN" + str(num)

def get_time():
    # current date and time using datetime module
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")

def get_fee(amount):
    # 2% fee, rounded up using math.ceil so we don't get decimals
    return math.ceil(amount * 0.02)


print("=== Welcome to QuickPay ===")
print("Time:", get_time())
print()

# step 1 - get wallet balance
try:
    wallet_balance = float(input("Enter your wallet balance: Rs."))
except ValueError:
    print("That's not a valid number. Exiting.")
    exit()

print(f"Wallet Balance: Rs.{wallet_balance}")
print()

# step 2 - PIN check (max 3 tries)
pin_ok = False

for attempt in range(1, 4):
    pin = input("Enter your PIN: ")

    try:
        if pin != correct_pin:
            raise WrongPINError("Wrong PIN!")   # raise sends us to except block

        # if we reach this line, pin was correct
        print("PIN accepted!")
        pin_ok = True
        break

    except WrongPINError as e:
        print(f"Error: {e} ({3 - attempt} tries left)")

if pin_ok == False:
    print("Too many wrong attempts. Exiting.")
    exit()

# step 3 - payment
print()

try:
    amount = float(input("Enter amount to pay: Rs."))

    # check 1 - amount should be more than 0
    if amount <= 0:
        raise BadAmountError("Amount must be greater than 0.")

    # check 2 - should have enough balance
    if amount > wallet_balance:
        raise LowBalanceError(f"You only have Rs.{wallet_balance} in your wallet.")

    # if both checks pass, do the payment
    fee = get_fee(amount)
    total = amount + fee
    wallet_balance = wallet_balance - total

    print()
    print("=== Payment Successful ===")
    print("Transaction ID :", get_txn_id())
    print("Time           :", get_time())
    print("Amount Paid    : Rs.", amount)
    print("Processing Fee : Rs.", fee)
    print("Total Deducted : Rs.", total)
    print("Balance Left   : Rs.", wallet_balance)
    print("==========================")

except BadAmountError as e:
    print("Amount Error:", e)

except LowBalanceError as e:
    print("Balance Error:", e)

except ValueError:
    # if user types letters instead of a number
    print("Please enter a valid number.")

finally:
    # finally block runs no matter what - success or failure
    print()
    print("Thank you for using QuickPay!")
    print("Session ended at:", get_time())