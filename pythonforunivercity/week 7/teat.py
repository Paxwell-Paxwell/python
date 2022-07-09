

def print_menu():
    print('Coffee Menu')
    print('1. Latte = 40 ')
    print('2. Espresso = 45')
    print('3. Americano = 50 ')
    print('4. Mocca = 55')
    print('5. Cappuccino = 60')
def order_coffee():
    order_dict = {}
    while True:
        ty = input('Coffee type: ')
        if ty == '0':
            break
        amount = int(input(f'Amount of {coffee[ty]}: '))
        if coffee[ty] not in order_dict.keys():
            order_dict[coffee[ty]] = amount
        else:
            order_dict[coffee[ty]] += amount
    total_price= 0
    for c,a in order_dict.items():
        total_price += pc[c]*a
    print(f'Total price: {total_price}')
    return order_dict,total_price
def change(total_price, pay) :
    cuschange = pay - total_price
    print(f'Customer\'s change: {cuschange}')
    if cuschange//1000 > 0 :
        print(f'Change 1000: {cuschange//1000}')
        cuschange = cuschange-cuschange//1000*1000
    if cuschange // 500 > 0:
        print(f'Change 500: {cuschange // 500}')
        cuschange = cuschange - cuschange // 500 * 500
    if cuschange // 100 > 0:
        print(f'Change 100: {cuschange // 100}')
        cuschange = cuschange - cuschange // 100 * 100
    if cuschange // 50 > 0:
        print(f'Change 50: {cuschange // 50}')
        cuschange = cuschange - cuschange // 50 * 50
    if cuschange // 20 > 0:
        print(f'Change 20: {cuschange // 20}')
        cuschange = cuschange - cuschange // 20 * 20
    if cuschange // 10 > 0:
        print(f'Change 10: {cuschange // 10}')
        cuschange = cuschange - cuschange // 10 * 10
    if cuschange // 5 > 0:
        print(f'Change 5: {cuschange // 5}')
        cuschange = cuschange - cuschange // 5 * 5
    if cuschange // 1 > 0:
        print(f'Change 1: {cuschange // 1}')
def print_receipt(orders_dict, customer_name, total_price):
    print('--------- receipt ---------')
    print('CPE35 COFFEE SHOP')
    print(f'Customer name: {customer_name}')
    for i in orders_dict.keys():
        print(f'{i} {orders_dict[i]}',end=',')
    print(f' {total_price} baht')
    print('Thank you')
    print('---------------------------')
def print_report(sales_dict):
    print('---- Daily Sale Report ----')
    totalsale = 0
    for name,tp in sales_dict.items():
        print(f'{name} {tp} baht')
        totalsale += tp
    print(f'Total sale: {totalsale} baht')
coffee = {'1':'Latte','2':'Espresso','3':'Americano','4':'Mocca','5':'Cappuccino'}
pc = {'Latte':40,'Espresso':45,'Americano':50,'Mocca': 55,'Cappuccino':60}
sales_dict = {}
while True:
    print_menu()
    customer_name = input("Customer name: ")
    if customer_name == "end day":
        break
    orders_dict, total_price = order_coffee()
    if customer_name not in sales_dict:
        sales_dict[customer_name] = total_price
    else:
        sales_dict[customer_name] += total_price

    pay = int(input("Customer pay: "))
    change(total_price,pay)
    print_receipt(orders_dict, customer_name, total_price)

print_report(sales_dict)

