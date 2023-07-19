# initialize variables
total_sales = 0
total_debts = 0
total_debt_payments = 0

# gas products
gas_products = {'Gasoline': {'price_per_unit': 0, 'total_units_sold': 0, 'debts': 0, 'debt_payments': 0},
                'Diesel': {'price_per_unit': 0, 'total_units_sold': 0, 'debts': 0, 'debt_payments': 0},
                'Kerosene': {'price_per_unit': 0, 'total_units_sold': 0, 'debts': 0, 'debt_payments': 0},
                'LPG': {'price_per_unit': 0, 'total_units_sold': 0, 'debts': 0, 'debt_payments': 0}}

# loop through each gas product

for product in gas_products:

    # get input from user for current gas product
    gas_products[product]['price_per_unit'] = float(input(f"Enter price per unit for {product}: "))
    gas_products[product]['total_units_sold'] = float(input(f"Enter total units sold for {product}: "))
    gas_products[product]['debts'] = float(input(f"Enter debts for {product}: "))
    gas_products[product]['debt_payments'] = float(input(f"Enter debt payments for {product}: "))

    # calculate sales for the current gas product
    sales = gas_products[product]['price_per_unit'] * gas_products[product]['total_units_sold']
    total_sales += sales
    total_debts += gas_products[product]['debts']
    total_debt_payments += gas_products[product]['debt_payments']

    # print sales for the current gas product
    print(f"Sales for {product}: {sales:.2f} dollars")

# print total sales, debts, and debt payments for the day
print(f"Total sales for the day: {total_sales:.2f} dollars")
print(f"Total debts for the day: {total_debts:.2f} dollars")
print(f"Total debt payments for the day: {total_debt_payments:.2f} dollars")