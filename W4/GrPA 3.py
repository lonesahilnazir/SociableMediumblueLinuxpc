min = None


def find_min(items: list):
    return sorted(items)[0]


def odd_increment_even_decrement_no_modify(items) -> list:
    newList = [i - 1 if i % 2 == 0 else i + 1 for i in items]
    return newList


def odd_square_even_double_modify(items: list) -> list:
    items[:] = [2 * i if i % 2 == 0 else i * i for i in items]
    return None


def more_than_two_unique_vowels(sentence):
    vowels = {"a", "e", "i", "o", "u"}
    words = sentence.split(",")
    moreVowels = {word for word in words if len(set(word) & vowels) > 2}
    return moreVowels


def sum_of_list_of_lists(lol):
    sum = 0
    for item in lol:
        for i in item:
            sum += i
    return sum


def flatten(lol):
    flattened = [i for sublist in lol for i in sublist]
    return flattened


def all_common(strings):
    common = set(strings[0])
    for word in strings[1:]:
        common &= set(word)
    return "".join(sorted(common))


def vocabulary(sentences):
    voc = set()
    for sentence in sentences:
        for word in sentence.split():
            voc.add(word.lower())
    return voc
