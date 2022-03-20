# Задача №1

name = input("Ваше имя: ")
age = input("Ваш возраст: ")
print(f"Приветствую, {name}, вам сейчас {age} лет.")


# Задача №2


import datetime
time = int(input("Здраствуйте, введите количество секунд : "))
print(f"Текущее количество секунд равна : {datetime.timedelta(seconds=time)}")


# Задача №3


number = input("Введите число: ")
total1 = int(number + number)
total2 = int(number + number + number)
compilate = int(number) + total1 + total2
print("Результат равен: ", compilate)


# Задача №4


number = input("Введите целое, положительное число :")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print(x)


# Задача №5


profit = int(input("Введите выручку фирмы: "))
costs = int(input("ВВедите издержки фирмы: "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила :{profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает без убытков")
else:
    print("Фирма работает с убытком")



# Задача №6


a = int(input("Введите резульат первого дня "))
b = int(input("Желаемый результат "))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
