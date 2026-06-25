# Product Inventory Processing Tool

import time


products = [
    {"name": "Laptop",     "price": 55000, "stock": 10, "category": "Electronics"},
    {"name": "Phone",      "price": 20000, "stock": 0,  "category": "Electronics"},
    {"name": "Desk Chair", "price": 8000,  "stock": 5,  "category": "Furniture"},
    {"name": "Headphones", "price": 3000,  "stock": 15, "category": "Electronics"},
    {"name": "Notebook",   "price": 100,   "stock": 50, "category": "Stationery"},
    {"name": "Pen",        "price": 20,    "stock": 0,  "category": "Stationery"},
    {"name": "Monitor",    "price": 15000, "stock": 3,  "category": "Electronics"},
    {"name": "Bookshelf",  "price": 5000,  "stock": 2,  "category": "Furniture"},
]


# decorator - wraps a function and prints how long it took to run
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  [{func.__name__} done in {round(end - start, 4)}s]")
        return result
    return wrapper


# generator - yields one product at a time instead of returning all at once
# good when list is huge, doesn't load everything into memory
def product_gen(plist):
    for p in plist:
        yield p

@timer
def available_products(plist):
    # filter + lambda - only in stock items
    return list(filter(lambda p: p["stock"] > 0, plist))


@timer
def prices_with_gst(plist):
    # map + lambda - 18% gst on every price
    return list(map(lambda p: round(p["price"] * 1.18, 2), plist))


@timer
def expensive_products(plist, min_price):
    # list comprehension
    return [p for p in plist if p["price"] >= min_price]


@timer
def all_names(plist):
    # list comprehension - just names
    return [p["name"] for p in plist]


@timer
def stock_dict(plist):
    # dict comprehension - name: stock
    return {p["name"]: p["stock"] for p in plist}


@timer
def unique_categories(plist):
    # set comprehension - no duplicates
    return {p["category"] for p in plist}


# lambda functions for sorting
sort_by_price = lambda plist: sorted(plist, key=lambda p: p["price"])
sort_by_stock = lambda plist: sorted(plist, key=lambda p: p["stock"], reverse=True)


@timer
def generate_report(plist):
    print()
    print("=" * 45)
    print("        INVENTORY REPORT")
    print("=" * 45)

    # using generator here
    gen = product_gen(plist)
    for p in gen:
        status = "In Stock" if p["stock"] > 0 else "Out of Stock"
        gst_price = round(p["price"] * 1.18, 2)
        print(f"  {p['name']:<15} | Rs.{p['price']:<7} | GST: Rs.{gst_price:<9} | Stock: {p['stock']:<4} | {status}")

    print("=" * 45)

    total = len(plist)
    out_of_stock = len([p for p in plist if p["stock"] == 0])
    inv_value = sum(p["price"] * p["stock"] for p in plist)

    print(f"  Total Products : {total}")
    print(f"  Available      : {total - out_of_stock}")
    print(f"  Out of Stock   : {out_of_stock}")
    print(f"  Total Value    : Rs.{inv_value}")
    print("=" * 45)


print("=== Inventory Tool ===")
print()

print(">> In Stock Products (filter + lambda):")
for p in available_products(products):
    print(f"   {p['name']} - stock: {p['stock']}")

print()
print(">> Prices with GST (map + lambda):")
gst = prices_with_gst(products)
for i in range(len(products)):
    print(f"   {products[i]['name']}: Rs.{gst[i]}")

print()
print(">> Products above Rs.5000 (list comprehension):")
for p in expensive_products(products, 5000):
    print(f"   {p['name']} - Rs.{p['price']}")

print()
print(">> All Names (list comprehension):")
print("  ", all_names(products))

print()
print(">> Stock Count (dict comprehension):")
for name, qty in stock_dict(products).items():
    print(f"   {name}: {qty}")

print()
print(">> Categories (set comprehension):")
print("  ", unique_categories(products))

print()
print(">> Sorted by Price (lambda):")
for p in sort_by_price(products):
    print(f"   {p['name']}: Rs.{p['price']}")

print()
print(">> Full Report (decorator + generator):")
generate_report(products)