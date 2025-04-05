def group_by(f, iterable):
    result = {}

    for item in iterable:
        key = f(item)
        if key not in result:
            result[key] = []
        result[key].append(item)

    return result

print(group_by(len, ["hi", "bye", "try"]))  # {2: ['hi'], 3: ['bye', 'try']}
