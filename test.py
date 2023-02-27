dict_object = [
    {"key1": "value1"},
    {"k1": "v1", "k2": "v2", "k3": "v3"},
    {},
    {},
    {"key1": "value1"},
    {"key1": "value1"},
    {"key2": "value2"}
]

known_dicts = set()
result = []
for d in dict_object:
    items = tuple(d.items())
    if items not in known_dicts:
        result.append(d)
        known_dicts.add(items)

print(result)