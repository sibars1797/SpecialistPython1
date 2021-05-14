# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def divmod_my(x, y):
    if y:
        unit = int(x/y)
        tail = int(y/abs(y))*(x - unit*y)
        if tail < 0:
            tail = tail - bool(unit)*2*tail
        return unit, tail
    else:
        print('В знаменателе не может быть "0"')

def simple_fractions(up, down):         #   приведение к наименьшему знаменателю
    for i in range(down, 1, -1):
        if not down % i and not up % i:
            down = int(down/i)
            up = int(up/i)
            return up, down
    return up, down

def part_str_to_int(symbols):           #   преобразование строки в числовую дробь
    res = {'up': 0, 'down': 1}
    whole = 0
    for part in symbols.split(' '):
        if part.find('/') == -1:
            whole = int(part)
        else:
            res['up'] = int(part.partition('/')[0])
            if whole < 0:
                res['up'] = - res['up']
            res['down'] = int(part.partition('/')[2])
    res['up'] = whole*res['down'] + res['up']
    simple_fractions(res['up'], res['down'])
    return tuple(res.values())

def fractions_transactions(line):       #   сложение/вычитание двух слагаемых
    if line.find(' + ', 2) > 1:
        parts = line.split(' + ')
        action = 1
    else:
        parts = line.split(' - ')
        action = -1
    up1 = part_str_to_int(parts[0])[0]
    down1 = part_str_to_int(parts[0])[1]
    up2 = part_str_to_int(parts[1])[0]
    down2 = part_str_to_int(parts[1])[1]
    if down1 and down2:
        up = up1*down2 + action*up2*down1
        down = down1*down2
#        unit = int(up/down)                                # когда divmod не работает
#        up, down = simple_fractions(up - down*unit, down)  # когда divmod не работает
#        if unit < 0:                                       # когда divmod не работает
#            up = -up                                       # когда divmod не работает
        unit, up = divmod_my(up, down)                 # divmod некорректно работает с отрицательными up, нужно понять
        up, down = simple_fractions(up, down)          # 
        wh_b = bool(unit)
        up_b = bool(up)
        return '0'*(not wh_b)*(not up_b) + (str(unit) + ' ')*wh_b + (str(up) + '/' + str(down))*up_b
    else:
        print('Ошибка: делитель(и) дроби = 0')
        return ''

print(fractions_transactions('-5/6 + 4/7'))
print(fractions_transactions('2/3 + -2/3'))
print(fractions_transactions('-3 2/3 + -1/3'))
print(fractions_transactions('-3 2/5 - -1/3'))
print(fractions_transactions('2/5 - -1/3'))
print(fractions_transactions('2/5 + 2/3'))


