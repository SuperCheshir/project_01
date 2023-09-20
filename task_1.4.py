# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}
# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.
store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}
# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

# Решение:

# boots_cost = store[titles['Кроссовки тип 3 (Adidas)']][31]['quantity'] * store[titles['Кроссовки тип 3 (Adidas)']][1637]['price']
# print('Кроссовки тип 3 (Adidas) -', 'quantity', 'шт, стоимость', boots_cost, 'руб')

# Решение:

print('Здравствуйте!')
boots_code = titles['Кроссовки тип 3 (Adidas)']
boots_item = store[boots_code][0]
boots_quantity = boots_item['quantity']
boots_price = boots_item['price']
boots_cost = boots_quantity * boots_price
print('Кроссовки тип 3 (Adidas) -', boots_quantity, 'шт, стоимость', boots_cost, 'руб')

ball_quantity_1 = store[titles['Мячик тип 2 (Adidas)']][0]['quantity']
ball_quantity_2 = store[titles['Мячик тип 2 (Adidas)']][1]['quantity']
ball_cost_1 = store[titles['Мячик тип 2 (Adidas)']][0]['quantity'] * store[titles['Мячик тип 2 (Adidas)']][0]['price']
ball_cost_2 = store[titles['Мячик тип 2 (Adidas)']][1]['quantity'] * store[titles['Мячик тип 2 (Adidas)']][1]['price']
print('Мячик тип 2 (Adidas) - ' + str(ball_quantity_1+ball_quantity_2) + ' шт, стоимость ' + str(ball_cost_1+ball_cost_2) + ' руб')

cap_quantity_1 = store[titles['Кепка тип 1 (Adidas)']][0]['quantity']
cap_quantity_2 = store[titles['Кепка тип 1 (Adidas)']][1]['quantity']
cap_cost_1 = store[titles['Кепка тип 1 (Adidas)']][0]['quantity'] * store[titles['Кепка тип 1 (Adidas)']][0]['price']
cap_cost_2 = store[titles['Кепка тип 1 (Adidas)']][1]['quantity'] * store[titles['Кепка тип 1 (Adidas)']][1]['price']
print('Кепка тип 1 (Adidas) - ' + str(cap_quantity_1+cap_quantity_2) + ' шт, стоимость ' + str(cap_cost_1+cap_cost_2) + ' руб')

belt_quantity_1 = store[titles['Ремень тип 2 (Nike)']][0]['quantity']
belt_quantity_2 = store[titles['Ремень тип 2 (Nike)']][1]['quantity']
belt_cost_1 = store[titles['Ремень тип 2 (Nike)']][0]['quantity'] * store[titles['Ремень тип 2 (Nike)']][0]['price']
belt_cost_2 = store[titles['Ремень тип 2 (Nike)']][1]['quantity'] * store[titles['Ремень тип 2 (Nike)']][1]['price']
print('Ремень тип 2 (Nike) - ' + str(belt_quantity_1+belt_quantity_2) + ' шт, стоимость ' + str(belt_cost_1+belt_cost_2) + ' руб')

shirt_quantity_1 = store[titles['Футболка тип 1 (Adidas)']][0]['quantity']
shirt_quantity_2 = store[titles['Футболка тип 1 (Adidas)']][1]['quantity']
shirt_quantity_3 = store[titles['Футболка тип 1 (Adidas)']][2]['quantity']
shirt_cost_1 = store[titles['Футболка тип 1 (Adidas)']][0]['quantity'] * store[titles['Футболка тип 1 (Adidas)']][0]['price']
shirt_cost_2 = store[titles['Футболка тип 1 (Adidas)']][1]['quantity'] * store[titles['Футболка тип 1 (Adidas)']][1]['price']
shirt_cost_3 = store[titles['Футболка тип 1 (Adidas)']][2]['quantity'] * store[titles['Футболка тип 1 (Adidas)']][2]['price']
print('Футболка тип 1 (Adidas) -', str(shirt_quantity_1+shirt_quantity_2+shirt_quantity_3),' шт, стоимость', str(shirt_cost_1+shirt_cost_2+shirt_cost_3), 'руб')

hat_code = titles['Шапка тип 5 (Puma)']
hats_item = store[hat_code][0]
hats_quantity = hats_item['quantity']
hats_price = hats_item['price']
hats_cost = hats_quantity * hats_price
print('Шапка тип 5 (Puma) -', hats_quantity, 'шт, стоимость', hats_cost, 'руб')
print('Готово!')