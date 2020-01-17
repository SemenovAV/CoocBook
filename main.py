from tools.get_shop_list_by_dishes import get_shop_list_by_dishes
from pprint import pprint

try:
   result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
except Exception as e:
    print(f'Ошибка: {e}')
