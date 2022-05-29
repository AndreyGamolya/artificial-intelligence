# 1 Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

f = open('test.txt', 'w')
li = input('Введите текст \n')
while li:
    f.writelines(li + '\n')
    li = input('Введите текст \n')
    if not li:
        break

#2 Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
#подсчёт строк и слов в каждой строке

def count():
    try:
        with open('test.txt', 'r', encoding = 'utf - 8') as f:
            li = f.readlines()
            for i in range(len(li)):
                new_li = li[i].split()
                print(f'Кол-во строк: {len(li)}, Кол-во слов {i + 1} строке: {len(new_li)}')
    except FileNotFoundError:
        return 'file not found'
count()

#3 Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.

with open('test.txt', 'r+') as f:
    st = list()
    for line in f.readlines():
        st.extend(line.rstrip().split(' '))
print(st)

print('ЗП меньше 20 тр: ')
summ = 0
for i in range (1, len(st), 2):
    zp = float(st[i])
    summ += zp
    q = len(st) / 2
    if zp <= 20000:
        print('*', st[i-1])
print(f'средняя величина ЗП: {summ/q}')

# 4 Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

def rewrite_file():
    num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []
    try:
        with open('file.txt', 'r+', encoding="utf-8") as file:
            with open('new_file.txt', 'w', encoding="utf-8") as new_file:
                l = file.readlines()
                for i in l:
                    i = i.split(' ', 1)
                    new_text.append(num[i[0]] + ' ' + i[1])
                new_file.writelines(new_text)
    except FileNotFoundError:
        return 'Файл не найден.'


rewrite_file()

# 5 Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()

# 6 Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
# были все типы занятий.

file = open("test.txt")
onstring = file.read().split("\n")[:-1]
print(onstring)

dict = {}

for item in onstring:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict[key] = value
print(dict)

print("\n<< Общее количество занятий по предметам >>")
for i in dict:
    list = dict[i]
    summ = 0
    for j in range(0, len(list)):
        summ += int(list[j])
    print(i, ":", summ)
file.close()