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
class WrongOTPError(Exception):
    pass


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
    # 2% fee, rounded up
    return math.ceil(amount * 0.02)
def get_otp():
    return random.randint(1000,9999)


print("=== Welcome to QuickPay ===")
print("Time:", get_time())
print()

# step 1 - get wallet balance
try:
    wallet_balance = float(input("Enter your wallet balance: Rs."))
except ValueError:
    print("That's not a valid number. Exiting.")
    exit()

print(f"Wallet Balance: Rs.{wallet_balance:.2f}")
print()

# step 2 - PIN check (max 3 tries)
pin_ok = False

for attempt in range(1, 4):
    pin = input("Enter your PIN: ")

    try:
        if pin != correct_pin:
            raise WrongPINError("Wrong PIN!")

        print("PIN accepted!")
        pin_ok = True
        break

    except WrongPINError as e:
        print(f"Error: {e} ({3 - attempt} tries left)")

if not pin_ok:
    print("Too many wrong attempts. Exiting.")
    raise WrongOTPError("too many attempts.failed")

# step 3 - payment
print()
otp=get_otp()
print("Generated OTP:",otp)
otp_ok=False
for attempt in range(1,4):
    entered_otp=input("Enter OTP:")
    try:
        if entered_otp!=str(otp):
            raise WrongOTPError("Wrong OTP")
        print("OTP verified")
        otp_ok=True
        break
    except WrongOTPError as e:
        print(f"Error:{e}({3-attempt}tries are left)")
if not otp_ok:
    print("otp error:otp verification failed.")
    raise WrongOTPError("too many attempts.failed")
    
    

try:
    amount = float(input("Enter amount to pay: Rs."))

    # check 1 - amount should be more than 0
    if amount <= 0:
        raise BadAmountError("Amount must be greater than 0.")
   

    # calculate fee and total deduction
    fee = get_fee(amount)
    total = amount + fee

    # check 2 - should have enough balance for amount + fee
    if total > wallet_balance:
        raise LowBalanceError(
            f"You need Rs.{total:.2f} including fee, but you only have Rs.{wallet_balance:.2f}."
        )

    # process payment
    wallet_balance = wallet_balance - total

    print()
    print("=== Payment Successful ===")
    print("Transaction ID :", get_txn_id())
    print("Time           :", get_time())
    print(f"Amount Paid    : Rs.{amount:.2f}")
    print(f"Processing Fee : Rs.{fee:.2f}")
    print(f"Total Deducted : Rs.{total:.2f}")
    print(f"Balance Left   : Rs.{wallet_balance:.2f}")
    print("==========================")
except WrongOTPError as e:
    print("OTP Error:",e)

except BadAmountError as e:
    print("Amount Error:", e)

except LowBalanceError as e:
    print("Balance Error:", e)

except ValueError:
    print("Please enter a valid number.")

finally:
    print()
    print("Thank you for using QuickPay!")
    print("Session ended at:", get_time())