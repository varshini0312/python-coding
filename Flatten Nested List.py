def flatten(nested_list):
    list_flat = []
    for item in nested_list:
        if isinstance(item, list):
            list_flat.extend(flatten(item))
        else:
            list_flat.append(item)
    return list_flat

print(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]
