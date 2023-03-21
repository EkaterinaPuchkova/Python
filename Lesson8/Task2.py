import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    with open('orders.json', 'w') as write_json:
        json.dump(data, write_json, indent=4)


write_order_to_json(
    item=['игрушки', 'книги', 'посуда'],
    quantity=[5, 4, 10],
    price=[100.00, 10.00, 50.50],
    buyer=['Василий Иванович'],
    date=['10.10.10'])