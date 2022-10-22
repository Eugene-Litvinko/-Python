#1. Вывести в консоль таблицу умножения на 4
def task_1():
    for i in range(1, 10):
        for j in range(1, 5):
            if i * j > 9:
                print(i, '*', j, '=', i * j, ' ', end='   ')
            else:
                print(i, '*', j, '=', i * j, ' ', end='    ')
        print('')

#2. Пользователь вводит число - х. Выводим в консоль все четные числа от нуля до х
def task_2(x):
    for i in range(0, (x + 1)):
        if i % 2 == 0:
            print(i, end = ' | ')
    return 0

#3. Пользователь вводит число - х. Выдаем число из последовательности фибоначчи с индексом х

def task_3(x):
    if x == 1 or x == 2:
        return 1
    return task_3(x - 1) + task_3(x - 2)

#4. Пользователь вводит число. Выводим в консоль факториал этого числа
def task_4(x):
    if x == 1:
        return 1
    return x*task_4(x - 1)
#5. Пользователь вводит строку. Выводим в консоль эту строку посимвольно (одна строка – один символ)
def task_5(str):
    for i in range(0, len(str)):
        print(str[i])
    return 0


def main():
   task_1()
   x = int(input('Enter number for task №2 =\n'))
   task_2(x)
   x = int(input('\nEnter number for task №3\n'))
   print(f'{x} - ый элемент последоватеьности = {task_3(x)}')
   x = int(input('Enter number for task №4\n'))
   print(f'Фактоориал числа {x} = {task_4(x)}')
   str = input('Enter string, please, for task №5 - ')
   task_5(str)

if __name__ == '__main__':
    main()