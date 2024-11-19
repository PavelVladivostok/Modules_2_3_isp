# 'Стиль кода часть 2'


# херовый способ выплнения домашнего задания

# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# i = 0
# while 0 < 12:  # true
#    i += 1
#    if i == 1:
#        print(my_list[0])
#    if i == 2:
#        print(my_list[1])
#    if i == 3:
#        print(my_list[2])
#    if i == 4:
#        print(my_list[3])
#    if i == 5:
#        continue
#        print(my_list[4])
#    if i == 6:
#        print(my_list[5])
#    if i == 7:
#        continue
#        print(my_list[6])
#    if i == 8:
#        break
#        print(my_list[7])
#    if i == 9:
#        print(my_list[8])
#    if i == 10:
#        print(my_list[9])
#    if i == 11:
#        continue
#        print(my_list[10])
#    if i == 12:
#        print(my_list[11])
# более или менее подходящий вариант !!!!! можно и переделать что бы использовать break


my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if i <= 5:
        if i != 4:
            print(my_list[i])
        i += 1
        continue
