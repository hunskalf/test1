# Задача №3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


number = input("Введите число: ")
total1 = int(number + number)
total2 = int(number + number + number)
compilation = int(number) + total1 + total2
print("Результат равен: ", compilation)
