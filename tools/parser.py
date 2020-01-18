def parser(file_data):
    data = file_data.read().split('\n')
    result = {}
    while data:
        next_recipe = int(data[1]) + 2
        recipe = data[:next_recipe:1]
        keys = ['ingredient_name', 'quantity', 'measure']
        result[recipe[0]] = list(
            map(lambda elem: {key: value for key, value in zip(keys, elem.split('|'))}, recipe[2:])
        )
        data = data[next_recipe + 1::1]
    return result
