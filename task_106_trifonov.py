# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Введите стартовый результат: '))
b = int(input('Введите нужный результат: '))
i = 0
while a < b:
    a = a + (a * 0.1)
    i += 1
print(i)

# загрузил задание 6 в репозиторий
