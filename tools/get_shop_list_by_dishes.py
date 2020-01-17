from tools.parser import parser


def get_shop_list_by_dishes(dishes, person_count):
    with open('./recipes.txt', 'r', encoding='utf-8') as f:
        book = parser(f)
        shop_list = dict()
        for dish in dishes:
            for ingredient in book.get(dish):
                name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity'])
                measure = ingredient['measure']
                list_item = shop_list.pop(name, {'measure': measure, 'quantity': 0})
                list_item['quantity'] += quantity * person_count
                shop_list[name] = list_item
        return shop_list
