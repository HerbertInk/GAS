# demo python code to calculate sales of a gas 
# station for the three products gasoline diesel and kerosene
# prints total sale debts and payments

# variables innit
total_sales = 0
total_debts = 0
total_debt_payments = 0

# gas products
gas_products = {'Gasoline': {'price_per_unit': 0, 'total_units_sold': 0, 'debts': 0, 'debt_payments': 0},
                'Diesel': {'price_per_unit': 0, 'total_units_sold': 0, 'debts': 0, 'debt_payments': 0},
                'Kerosene': {'price_per_unit': 0, 'total_units_sold': 0, 'debts': 0, 'debt_payments': 0}}

# looping through each gas product

for product in gas_products:

    # get input from user for current gas product
    gas_products[product]['price_per_unit'] = float(input(f"Unit price {product}: "))
    gas_products[product]['total_units_sold'] = float(input(f"Units sold {product}: "))
    gas_products[product]['debts'] = float(input(f"Debts {product}: "))
    gas_products[product]['debt_payments'] = float(input(f"Payments {product}: "))

    # calculate sales for the current gas product
    sales = gas_products[product]['price_per_unit'] * gas_products[product]['total_units_sold']
    total_sales += sales
    total_debts += gas_products[product]['debts']
    total_debt_payments += gas_products[product]['debt_payments']

    # sales for the current gas product
    print(f"Sales for {product}: {sales:.2f} dollars")

# print total sales, debts, and debt payments for the day
print("\n SALES FOR THE DAY \n")
print(f"Debts for the day: ${total_debts:.2f}")
print(f"Payments: ${total_debt_payments:.2f}")
print(f"Sales for the day: ${total_sales:.2f}")

"""
    this is all going incremental
"""