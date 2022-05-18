# ex.1
age = 30
weight = 80
print(age, weight)

age = input('Введите свой возраст: ')
weight = input('Введите свой вес: ')
print('Ваш возраст: ', age,'Ваш вес: ', weight)


# ex.2
sec = int(input('Введите время в секундах: '))
h = sec // 3600
m = (sec - h * 3600 ) // 60
s = (sec - h * 3600) - m * 60
print("{0} : {1} : {2}.".format(h,m,s))

# ex.3

n = (input('Введите число n: '))
x = n + n
y = n + n + n
print("Тогда n + nn + nnn = ", int(n) + int(x) + int(y))

# ex.4

n = int(input("Введите целое положительное число: "))
M = 0
while n > 0:
    d = n % 10
    if d > M:
        M = d
    n = n // 10
print(M)

# ex.5

r = int(input('Выручка, т.р.: '))
c = int(input('Издержки, т.р.: '))
p = r - c
if p > 0:
    print('Ваша компания прибыльна !, Рентабельность: ', p/r*100 , '%')
else:
    print('Ваша компания убыточна! Вы потеряли:', p , 'т.р.')

# ex. 6

a = 2
b = 3
day = 1
while a < b:
    a *= 1.1
    day += 1
print(day , '-й день, когда достиг 3х км')


