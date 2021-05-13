# Дан файл ("data/fruits.txt") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов и
# распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

first_symb_fruits = {}                                                    # формирование словаря с ключами от "А" до "Я"
for symb in list(map(chr, range(ord('А'), ord('Я') + 1))):                #
    first_symb_fruits.update([(symb, [])])                                #
#first_symb_fruits = dict.fromkeys(list(map(chr, range(ord('А'), ord('Я') + 1))), [])   #при таком способе создания словаря метод append работает неожиданно, надо разбираться
with open('data/fruits.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
#            first_symb.setdefault(line[0], [])   #если не обязательно делать файл с каждой буквой, данный метод позволяет обойтись без предаварительного создания словаря
            first_symb_fruits[line[0]].append(line + '\n' + '\n')
for symb in first_symb_fruits:
    with open(f'data/fruits/fruits_{symb}.txt', 'w', encoding='utf-8') as f:
        print(*(first_symb_fruits[symb]), file=f)
