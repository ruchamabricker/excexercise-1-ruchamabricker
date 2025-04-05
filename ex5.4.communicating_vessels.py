def interleave(*quantities):
    if not quantities:
        return None

    zipped = list(zip(*quantities))
    result = []

    for group in zipped:
        for item in group:
            result.append(item)

    return result


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
