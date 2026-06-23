# Food Ordering System

MENU = {
    "burger": 120,
    "pizza": 250,
    "pasta": 180,
    "fries": 60,
    "coke": 40,
    "sandwich": 100,
    "noodles": 130,
    "ice cream": 80,
}

order_list = []  


def show_menu():
    # just prints whatever is in MENU dict
    # no params needed since MENU is global
    print("\n-------- MENU --------")
    for item, price in MENU.items():
        print(f"  {item.capitalize()} - Rs.{price}")
    print("----------------------")


def get_price(item_name):
    

    return MENU.get(item_name.lower())


def add_item(item_name, qty):
    
    price = get_price(item_name)

    if price is None:
        return False

    
    entry = {
        "name": item_name.lower(),
        "qty": qty,
        "price": price,
        "subtotal": price * qty
    }
    order_list.append(entry)
    return True


def calculate_total(*items):
    
    total = 0
    for item in items:
        total += item["subtotal"]
    return total


def apply_discounts(**kwargs):
    """
    applies discounts based on what flags are passed in
    
    accepted kwargs:
        amount     - bill amount (required)
        is_student - True/False, gives 5% off
        has_coupon - coupon code string, 'SAVE20' gives 20% off
        is_bulk    - True/False, 10% off if qty > 5
    
    returns (final amount, total discount)
    """
    amount = kwargs.get("amount", 0)
    discount = 0

    # student discount
    if kwargs.get("is_student"):
        discount += amount * 0.05
        print("  Student discount applied: 5%")

    # bulk order discount
    if kwargs.get("is_bulk"):
        discount += amount * 0.10
        print("  Bulk order discount applied: 10%")

    # coupon
    coupon = kwargs.get("has_coupon", "")
    if coupon.upper() == "SAVE20":
        discount += amount * 0.20
        print("  Coupon SAVE20 applied: 20%")
    elif coupon != "":
        
        print(f"  '{coupon}' is not a valid coupon, skipping")

    final = amount - discount
    return round(final, 2), round(discount, 2)


def show_bill(cust_name, total, discount, final):
    
    print()
    print("=" * 38)
    print(f"  ORDER SUMMARY for {cust_name.title()}")
    print("=" * 38)

    for entry in order_list:
        
        item_label = entry["name"].title()
        line = f"  {item_label} x{entry['qty']}  ->  Rs.{entry['subtotal']}"
        print(line)

    print("-" * 38)
    print(f"  Subtotal    :  Rs.{total}")
    if discount > 0:
        print(f"  Discount    : -Rs.{discount}")
    print(f"  Total       :  Rs.{final}")
    print("=" * 38)


def confirm(cust_name, amount):
   
    print(f"\nOrder confirmed for {cust_name.title()}!")
    print(f"Please pay Rs.{amount} at the counter.")
    print("Estimated time: 20-25 mins\n")



print("Welcome to QuickBites!")

name = input("Enter your name: ").strip()

show_menu()

print("\nStart adding items to your order.")
print("Type 'done' when finished.\n")

while True:
    item = input("Item name: ").strip()

    if item.lower() == "done":
        if len(order_list) == 0:
            print("Please add at least one item first.")
            continue
        break

    try:
        qty = int(input(f"Quantity for {item}: "))
        if qty <= 0:
            print("Quantity has to be 1 or more.")
            continue
    except ValueError:
        print("Enter a number for quantity.")
        continue

    success = add_item(item, qty)
    if success:
        print(f"Added {item.title()} x{qty}\n")
    else:
        print(f"'{item}' is not on the menu, try again.\n")


raw_total = calculate_total(*order_list)

print()
student_ans = input("Are you a student? (yes/no): ").strip().lower()
is_student = student_ans == "yes"

coupon_code = input("Coupon code (press Enter if none): ").strip()


total_qty = sum(e["qty"] for e in order_list)
is_bulk = total_qty > 5


print("\nApplying discounts...")
final_amount, discount_amount = apply_discounts(
    amount=raw_total,
    is_student=is_student,
    has_coupon=coupon_code,
    is_bulk=is_bulk
)

show_bill(name, raw_total, discount_amount, final_amount)
confirm(name, final_amount)