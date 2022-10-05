# step 8
def draw_box():
    for i in range(14):
        if i == 0 or i == 13:
            print('*' * 10)
        else:
            print('*', ' ' * 6, '*')


draw_box()


# step 9
def draw_triangle():
    print(*['*' * i for i in range(1, 11)], sep='\n')


draw_triangle()
