name = input("Enter Customer name: ")
place = input("Enter Customer's state: ")
invoice_no = input("Enter Invoice number: ")
products = []
quantities = []
prices = []
inventory = {}
total_prices = []
total_price = 0

def inventory_choice():
    i = 1
    while True:
        item = input(f"Enter product {i} name. Enter e to exit: ")

        if item.lower() == 'e':
            break

        quantity = int(input(f"Enter quantity of {item}: "))
        price = int(input(f"Enter price of 1 quantity of {item}: "))
        i+=1

        products.append(item)
        quantities.append(quantity)
        prices.append(price)

inventory_choice()

if not products:
    choice = input("Are you sure you have no products? (y/n): ")
    if choice.lower() == 'n':
        inventory_choice()

for q, p in zip(quantities, prices):
    price = q*p

    total_prices.append(price)

for n, q, p, tp in zip(products, quantities, prices, total_prices):
    inventory[n] = {"quantity": q, "price": p, "amount": tp}

for i in total_prices:
    total_price+=i

discount = int(input("Enter discount percentage: "))
discount_amount = discount/100 * total_price
taxable_price = total_price - discount_amount

print()
print("Assuming business to be located at Kerala with 18% GST")
print()
print('''SDV Traders
         Alappuzha, Kerala - 688001
         TAX INVOICE''')
print('--------------------')
print("Invoice Details")
print('--------------------')
print(f'''Particulars              Details

Invoice Number:          {invoice_no}
Invoice Date:            07/11/2026
Payment Mode:            Bank Transaction''')
print()
print("Buyer Details")
print('--------------------')
print(f'''Particulats              Details

Customer Name            {name}
Place                    {place}''')
print()
print("Product Details")
print('--------------------')
print(f'Product                    Quantity       Rate      Amount')
print()
item_space, space, qty_space, rate_space, amt_space = " "*27, " "*2, " "*12, " "*8, " "*9
for item in inventory:
    item_space = item + ((len(item_space) - len(item))*" ")
    qty_space = str(inventory[item]["quantity"]) + ((len(qty_space) - len(str(inventory[item]["quantity"])))*" ")
    rate_space = str(inventory[item]["price"]) + ((len(rate_space) - len(str(inventory[item]["price"])))*" ")
    amt_space = str(inventory[item]["amount"]) + ((len(amt_space) - len(str(inventory[item]["amount"])))*" ")
    string = item_space + space + qty_space + space + rate_space + space + amt_space
    print(string)
print()
print(f"Subtotal is {total_price}")
print()
print("Discount Calculation")
print('--------------------')
print(f'''Particulars              Details

Subtotal:                {total_price}
Discount ({discount}%):          {discount_amount}
Taxable Value:           {taxable_price}''')
print()
print("GST Calculation")
print('--------------------')
if place.lower() == 'kerala':
    CGST = round(9/100 * taxable_price, 2)
    SGST = round(9/100 * taxable_price, 2)
    GST = CGST + SGST
    final_value = GST + taxable_price

    print(f'''Particulars              Details

CGST (9%):               {CGST: .2f}
SGST (9%):               {SGST: .2f}
Total GST:               {GST: .2f}''')
    print()
    print(f"Grand Total: {final_value}")

else:
    GST = IGST = round(18/100 * taxable_price, 2)
    final_value = GST + taxable_price

    print(f'''Particulars              Details

    IGST (18%):              {IGST: .2f}
    Total GST:               {GST: .2f}''')
    print()
    print(f"Grand Total: {final_value}")
print()
print('--------------------')
print("Customer Signature                   Authorized Signatory")
print("Thankyou for your purchase")
