# step 8
def draw_triangle(fill1, base1):
    for i in range(1, base1 // 2 + 2):
        print(i * fill1)
    for j in range(base1 // 2, 0, -1):
        print(j * fill1)


fill = input()
base = int(input())

draw_triangle(fill, base)


# step 9
def print_fio(name1, surname1, patronymic1):
    print(surname1[0].upper(), name1[0].upper(), patronymic1[0].upper(), sep='')


name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)


# step 10
def print_digit_sum(num):
    nell = [int(i) for i in str(num)]
    print(sum(nell))


n = int(input())

print_digit_sum(n)
