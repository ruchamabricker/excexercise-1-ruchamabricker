def interleave(*quantities):
    if not quantities:
        return None

    zipped = list(zip(*quantities))
    result = []

    for group in zipped:
        for item in group:
            result.append(item)

    return result

if __name__ == "__main__":
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
