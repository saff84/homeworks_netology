# Задача 1

FILE_NAME = 'recipes.txt'
cook_book = {}
list_keys = ['ingredient_name', 'quantity', 'measure']


def file_worker(file_name):
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            line_1 = file.readline()
            cook_book[line.strip()] = []
            for i in range(int(line_1.strip()) + 1):
                line2 = file.readline()
                if line2.strip() != '':
                    list_ingridients = line2.strip().split(' | ')
                    dict_ingridients = dict(zip(list_keys, list_ingridients))
                    cook_book[line.strip()].append(dict_ingridients)

                else:
                    continue

        return cook_book


file_worker(FILE_NAME)
# print(cook_book)

# Задача 2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    # print(cook_book.keys())
    for i in dishes:
        # print(i)
        for items in cook_book.keys():
            # print(items)
            if items == i:
                for dish in cook_book[items]:

                    if dish['ingredient_name'] not in shop_list.keys():
                        shop_list[dish.get('ingredient_name')]= {dish.get('measure'): (int(dish.get('quantity')) * person_count)}
                    else:

                        shop_list[dish['ingredient_name']][dish.get('measure')] =  int(shop_list[dish['ingredient_name']][dish.get('measure')]) + (int(dish.get('quantity')) * person_count)
    return shop_list

# print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))

#Задача 3
FILE_NAME_1 = '1.txt'
FILE_NAME_2 = '2.txt'
FILE_NAME_3 = '3.txt'
file_name_4 = '4.txt'



def file_worker_2(file_name_1,file_name_2,file_name_3):
    with open(file_name_1, encoding = "utf-8") as f:
        file1 = f.read().split('\n')
        # print(file1)
        # print(len(file1))

    with open(file_name_2, encoding = "utf-8") as f:
        file2 = f.read().split('\n')
        # print(len(file2))

    with open(file_name_3, encoding = "utf-8") as f:
        file3 = f.read().split('\n')
        # print(len(file3))

    files_list = [[file1, file_name_1], [file2, file_name_2], [file3, file_name_3]]
    files_list = sorted(files_list, key = lambda i : len(i[0]))
    # print(files_list)

    with open(file_name_4,"w", encoding="utf-8") as f:
        for i in files_list:
            # print(str(i).replace("[","").replace("]","").replace("'",""))
            f.write(f'{i[1]}\n{len(i[0])}\n{str(i[0]).replace("[","").replace("]","")}\n')
# Только не понимаю как от скобок избавиться и построчно записать

file_worker_2(FILE_NAME_1, FILE_NAME_2, FILE_NAME_3)

