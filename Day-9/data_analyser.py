# Data Analyzer Utility Program
# Day 9 - mutable/immutable, memory, copy, collections module

import copy
from collections import Counter, defaultdict

# mutable vs immutable
print("=== Mutable vs Immutable ===")

a = 10
b = a
b = 20
print(f"a = {a}, b = {b}")
print("b changed but a stayed same - ints are immutable\n")

list1 = [1, 2, 3]
list2 = list1   # not a copy, both pointing to same list
list2.append(4)
print("list1:", list1)
print("list2:", list2)
print("changed list2 but list1 changed too lol - lists are mutable\n")


# memory reference
print("=== Memory Reference ===")

x = [1, 2, 3]
y = x
print("id of x:", id(x))
print("id of y:", id(y))
print("same id, x and y are literally the same list in memory\n")

z = [1, 2, 3]
print("id of z:", id(z))
print("different id even tho values look identical\n")


# copy module
print("=== Copy module ===")

original = [1, 2, [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0] = 100
shallow[2].append(999)   # this messes with original too, shallow copy issue

print("original:", original)
print("shallow :", shallow)
print("shallow copy only copies outer list, inner list still shared\n")

deep[0] = 500
deep[2].append(777)
print("after deepcopy:")
print("original:", original)
print("deep    :", deep)
print("deepcopy is fully independent, even nested stuff\n")


# collections module
print("=== Collections module ===")

products_sold = ["pizza", "burger", "pizza", "pasta", "burger", "pizza"]
count_result = Counter(products_sold)
print("Counter:", count_result)
print("most sold:", count_result.most_common(1))
print()

# defaultdict so we dont get keyerror when key doesnt exist yet
student_marks = defaultdict(list)
student_marks["Mridula"].append(85)
student_marks["Mridula"].append(90)
student_marks["Mridula"].append(70)

print("defaultdict:", dict(student_marks))
print("no need to check if key exists before appending\n")


# mini analyzer combining everything
print("=== Mini Data Analyzer ===")

sales_data = [
    {"product": "Laptop", "qty": 2},
    {"product": "Phone", "qty": 5},
    {"product": "Laptop", "qty": 1},
    {"product": "Tablet", "qty": 3},
    {"product": "Phone", "qty": 2},
]

totals = defaultdict(int)
for entry in sales_data:
    totals[entry["product"]] += entry["qty"]

print("Total qty sold per product:")
for product, qty in totals.items():
    print(f"  {product}: {qty}")

product_names = [entry["product"] for entry in sales_data]
order_count = Counter(product_names)
print("\nMost ordered product:", order_count.most_common(1)[0])

print()
print("pip and venv part is just terminal commands, putting it as comments below")
print("since it's not actual python code")

# pip/venv notes
# pip = installs external packages eg: pip install requests
# venv = creates a separate python environment so packages dont clash between projects
#
# create venv: python -m venv myenv
# activate (windows): myenv\Scripts\activate
# activate (mac/linux): source myenv/bin/activate
# install package: pip install package_name
# see installed packages: pip list
# save dependencies to file: pip freeze > requirements.txt
# install from that file: pip install -r requirements.txt