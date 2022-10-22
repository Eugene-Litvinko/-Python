from array import *

#1. Дан массив с целыми числами. Вывести в консоль количество положительных и отрицательных чисел в нем

def task_1(data):
    sum_negative = 0
    sum_positive = 0
    for i in range(0, len(data)):
        if data[i] < 0:
            sum_negative += 1
        else:
            sum_positive += 1
    return sum_negative, sum_positive

#2. Дан массив с целыми числами. Вывести в консоль сумму элементов с четными индексами
def task_2(data):
    sum = 0
    for i in range(0, len(data)):
        if i % 2 == 0:
            sum += data[i]
        else:
            pass
    return sum

#3. Дан массив с целыми числами. Вывести в консоль сумму четных элементов (четные значения)
def task_3(data):
    sum = 0
    for i in range(0, len(data)):
        if data[i] % 2 == 0:
            sum += data[i]
        else:
            pass
    return sum

#4. Дан массив с целыми числами. Вывести в консоль наибольшее из них
#5. Дан массив с целыми числами. Вывести в консоль наиболее часто встречающееся. Если таких несколько, то вывести наибольшее из них, если повторяющихся нет, вывести соответствующее сообщение.

def task_5(data):
    d = {}
    for i in range(0, len(data)):
        if data.count(data[i]) != 1:
            d[data[i]] = data.count(data[i])
        else:
            pass
    if not d:
        return print('Повторящихся элементов в массиве нет')
    else:
        return print (f'Число {d.get(max(d.values()))} входит {max(d.values())} раз в массив') # не допилил сравнение ключей, если количество вхождений одинаково


def main():
    data = array('i', [2, 5, 4, 0, 8, -4, -8, 0, 2, 4, 4, 4])
    print(f'Количество отрицательных чисел = {task_1(data)[0]}\nКоличество положительных чисел = {task_1(data)[1]}')  #до этого задания не знал что возможно так обращаться к значениям, которые вовращает функция ))
    print(f'Сумма элементов массива c четным индексом = {task_2(data)}')
    print(f'Сумма четных элементов массива = {task_3(data)}')
    print(f'Наибольшое значение в массиве = {max(data)}')
    task_5(data)


if __name__ == '__main__':
    main()