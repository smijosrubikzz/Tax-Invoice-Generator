name = input("Enter Customer name: ")
place = input("Enter Customer's state: ")
invoice_no = input("Enter Invoice number: ")
products = []
i = 1
quantities = []
prices = []
inventory = {}
total_prices = []
total_price = 0

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

for n, q, p in zip(products, quantities, prices):
    inventory[n] = {"quantity": q, "price": p}

for i in inventory:
    price = inventory[i]["quantity"]*inventory[i]["price"]

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
Invoice Date:            06/11/2026
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
for i in inventory:
    print(f'{i}         {inventory[i]["quantity"]}               {inventory[i]["price"]}         {inventory[i]["amount"]}')
print()
print(f"Subtotal is {total_price}")
print()
print("Discount Calculation")
print('--------------------')
print(f'''Particulars              Details

Subtotal:                {total_price}
Discount ({discount}%):          {discount_amount}
Taxable Value:            {taxable_price}''')
print()
print("GST Calculation")
print('--------------------')
if place.lower() == 'kerala':
    CGST = 9/100 * taxable_price
    SGST = 9/100 * taxable_price
    GST = CGST + SGST

    final_value = GST + taxable_price

    print(f'''Particulars              Details

CGST (9%):               {CGST}
SGST (9%):               {SGST}
Total GST:               {GST}''')
    print()
    print(f"Grand Total: {final_value}")

else:
    GST = IGST = 18/100 * taxable_price

    final_value = GST + taxable_price

    print(f'''Particulars              Details

    IGST (18%):              {IGST}
    Total GST:               {GST}''')
    print()
    print(f"Grand Total: {final_value}")
print()
print('--------------------')
print("Customer Signature                   Authorized Signatory")
print("Thankyou for your purchase")
