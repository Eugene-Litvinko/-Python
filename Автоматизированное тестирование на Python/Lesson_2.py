# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def chek_Availability_porridge():
    porridge = input('Укажите номер каши, которую хотим приготовть?\n1.Гречка\n2.Рис\n3.Овсянка\n4.Другая каша\n5.Каши нету\n')
    return int(porridge)

def prepare_porridge(weight):
    v_castrly = 3000
    print(f'Необходимо взять кастрюлю и налить воды в пропорции 1:3, т.е. {weight*3} мл')
    if weight + weight*3 > v_castrly:
        print('Необходимо заменить кастрю')
    print('Спасибо! Теперь поставим кастрюлю на плиту и ждем 1 мин')
    for j in range(1, 10):
        print(f'Прошло {j} минут')
    print('Вода закипела!!!\nНебходимо засыпать кашу в кастрюлю с водой, котора стоит на плите')


def main():
    i = True
    while i:
        porridge = chek_Availability_porridge()
        porridges = {
            1: 'Гречка',
            2: 'Рис',
            3: 'Овсянка',
            4: 'Другая каша',
            5: 'Каши нету',
        }
        try:
            if porridge != 5:
                print(f'Здорово! У тебя есть {porridges[porridge]}')
                weight = input('Укажите количество каши в граммах\n')
                weight = int(weight)
                prepare_porridge(weight)
            elif porridge == 5:
                print(f'Вам необходимо купить одну из каш и вернуться к нам')
                i = False
        except:
            print('Ввели неправильный номер. Доступные цифры для ввода: 1,2,3,4,5.\nЗапустите программу снова')
            i = False
if __name__ == '__main__':
    print('Вас приветствует алгоритм под названием "Готовка каши"')
    main()

