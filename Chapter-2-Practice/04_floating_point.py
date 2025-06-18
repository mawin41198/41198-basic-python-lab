sales_input = input()

sales = float(sales_input)

commission = sales * 3.5 / 100

commission_rounded = round(commission, 2)
print(commission_rounded)