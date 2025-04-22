def join(*lists, sep=None):
    if len(lists) == 0:
        return None

    result = []
    for i, lst in enumerate(lists):
        if not isinstance(lst, list):
            print("All arguments must be lists")
            return None
        result.extend(lst)
        if sep is not None and i < len(lists) - 1:
            result.append(sep)

    return result

def main():
    print(join([1], [2], [3], sep='@'))

    print(join([5, 6, 9], [8], [12]))

    print(join([1]))

    print(join())

main()