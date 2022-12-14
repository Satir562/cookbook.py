from pprint import pprint
file_path = 'cookbook.txt'
def make_cook_book(name_file):
    cook_book = {}
    with open(name_file, encoding='UTF-8') as file:
        for line in file:
            dish = line.strip()
            number_ingredients = int(file.readline())
            ingredients_list = []
            for item in range(number_ingredients):
                ingr = file.readline().split(' | ')
                ingredients = {"ingredient_name": ingr[0].strip(), "quantity": int(ingr[1]), "measure": ingr[2].strip()}
                ingredients_list.append(ingredients)
            cook_book[dish] = ingredients_list
            file.readline()
    return cook_book



def get_shop_list_by_dishes(dishes: list, person_count):
    cook_book = make_cook_book(file_path)
    shop_list = {}
    for dish in dishes:
        for ingredients in cook_book.get(dish, []):
            if dish[0] in shop_list:
                shop_list[ingredients[dishes]]['quantity'] += ingredients['quantity'] * person_count
            else:
                shop_list[ingredients['ingredient_name']] = {'quantity': ingredients['quantity'] * person_count, 'measure': ingredients['measure']}
    return shop_list
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))