total_price = int(input('Введите общую стоимость часов'))
silver = 48
gold = (total_price - 96 * silver) / 16
print('Цена золотых часов', int(gold))