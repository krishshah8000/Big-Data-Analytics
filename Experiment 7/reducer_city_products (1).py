#!/usr/bin/env python3
import sys

current_key = None
total_sales = 0.0
city_data = {}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    key, price = line.split('\t')
    price = float(price)
    if current_key is None:
        current_key = key
        total_sales = price
    elif key == current_key:
        total_sales += price
    else:
        city, product = current_key.split('_')
        if city not in city_data:
            city_data[city] = []
        city_data[city].append((product, total_sales))
        current_key = key
        total_sales = price

# Process the final trailing key pair
if current_key is not None:
    city, product = current_key.split('_')
    if city not in city_data:
        city_data[city] = []
    city_data[city].append((product, total_sales))

# Print structured metrics results 
print("TOP PRODUCT PER CITY:")
print("=" * 40)
for city in city_data:
    city_data[city].sort(key=lambda x: x[1], reverse=True)
    top_product = city_data[city][0]
    print(f"{city}: {top_product[0]} (₹{top_product[1]:,.2f})")