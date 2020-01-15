def parser(data):
    result = {}
    key_counter = 0
    ingredient_counter = None
    key = None
    while True:
        line = data.readline()
        if not line:
            break
        elif key_counter == 1 and line == '\n':
            key_counter = 0
            ingredient_counter = None
            key = None
            continue
        elif key_counter == 0:
            result.setdefault(line.strip(), [])
            key = line.strip()
            key_counter += 1
            continue
        elif key_counter == 1 and not ingredient_counter:
            ingredient_counter = int(line)
            continue
        elif key_counter == 1 and ingredient_counter:
            keys = ['ingredient_name', 'quantity', 'measure']
            values = line.strip().split('|')
            ingredient = {a: b for a, b in zip(keys, values)}
            result.get(key, []).append(ingredient)
            ingredient_counter -= 1

    return result
