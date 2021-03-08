profit = float(input("Выручка"))
costs= float(input("Издержки"))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность {profit / costs}")
    workers = int(input("Введите количество сотрудников"))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")