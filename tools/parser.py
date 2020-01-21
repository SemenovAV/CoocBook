def parser(file_data):
    data = file_data.read().split('\n')
    result = {}
    while data:
        next_recipe = int(data[1]) + 2
        recipe = data[:next_recipe]
        keys = ['ingredient_name', 'quantity', 'measure']
        result[recipe[0]] = list()
        for elem in recipe[2:]:
            result[recipe[0]].append(
                dict(zip(keys, elem.split('|'))))
        data = data[next_recipe + 1:]
    return result
