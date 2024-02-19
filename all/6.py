height=float(input('Введите рост в дюймах:'))
weight=float(input('Введите вес в фунтах:'))
IMT=(weight/(height**2))
print("Индекс массы тела:{:.2f}".format(IMT))