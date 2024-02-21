height=float(input('Введите рост в дюймах:'))
weight=float(input('Введите вес в фунтах:'))
centimetre=0,39*height
kilo=weight*0,45
IMT=(kilo/(centimetre**2))
print("Индекс массы тела:{:.2f}".format(IMT))