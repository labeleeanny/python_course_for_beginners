# task 4
def draw_triangle():
    for i in range(8):
        print(' ' * (8 - 1 - i) + '*' * (1 + i * 2))


draw_triangle()


# task 5
def get_shipping_cost(quantity):
    return 1000 + (quantity - 1) * 120


n = int(input())

print(get_shipping_cost(n))

# task 6
from math import factorial


def compute_binom(n1, k1):
    return int(factorial(n1) / (factorial(k1) * factorial(n1 - k1)))


n = int(input())
k = int(input())

print(compute_binom(n, k))


# task 7
def number_to_words(num1):
    s = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
         'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
         'девятнадцать', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
         'девяносто', '']
    if num1 <= 20:
        return s[num1 - 1]
    else:
        return s[num1 // 10 - 1 + 18] + ' ' + s[num1 % 10 - 1]


n = int(input())

print(number_to_words(n))


# task 8
def get_month(language, number):
    ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
          'декабрь']
    en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
          'december']
    if language == 'ru':
        return ru[number - 1]
    elif language == 'en':
        return en[number - 1]


lan = input()
num = int(input())

get_month(lan, num)
print(get_month(lan, num))


# task 9
def is_magic(date1):
    t = date1.split('.')
    a = t[0]
    b = t[1]
    c = t[2]
    if int(a) * int(b) == (int(c) % 100):
        return True
    else:
        return False


date = input()

print(is_magic(date))


# task 10
def is_pangram(text1):
    res = True
    c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    y = text1.lower()
    t = list(y)
    for i in range(len(c)):
        if not c[i] in t:
            res = False
            break
    return res


text = input()

print(is_pangram(text))
