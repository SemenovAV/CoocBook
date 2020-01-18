from tools.get_shop_list_by_dishes import get_shop_list_by_dishes
from tools.parser import parser
from pprint import pprint

with open('./recipes.txt', 'r', encoding='utf-8') as f:
    print('Задание 1:')
    pprint(parser(f))
    print('Задание 2:')
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
