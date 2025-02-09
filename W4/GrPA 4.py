def swap_halves(items):
    lenght = len(items)
    half = lenght // 2
    newTuple = items[half:] + items[:half]
    return newTuple


def swap_at_index(items, k):
    lenght = len(items)
    newTuple = items[k + 1 : lenght] + items[: k + 1]
    return newTuple


def rotate_k(items, k=1):
    k = k % len(items)
    newList = items[-k:] + items[:-k]
    return newList


def first_and_last_index(items, elem):
    first_index = items.index(elem)
    rev = items[::-1]
    last_index = (len(items) - 1) - rev.index(elem)
    return (first_index, last_index)


def reverse_first_and_last_halves(items):
    half = len(items) // 2
    items[:half] = items[:half][::-1]
    items[half:] = items[half:][::-1]
