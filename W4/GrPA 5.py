def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)


def total_cost(cart):
    return sum(x[0] * x[1] for x in cart)


def abbreviation(sentence):
    return "".join((word[0].upper() + ".") for word in sentence.split())


def palindromes(words):
    return [word for word in words if word == word[::-1]]


def all_chars_from_big_words(sentence):
    return set("".join(word.lower() for word in sentence.split() if len(word) > 5))


def flatten(lol):
    return [x for sublist in lol for x in sublist]


def unflatten(items, n_rows):
    length = len(items)
    columns = length // n_rows
    return [items[i * columns : (i + 1) * columns] for i in range(n_rows)]


def make_identity_matrix(m):
    return [[1 if i == j else 0 for i in range(m)] for j in range(m)]


def make_lower_triangular_matrix(m):
    return [[i + 1 if i <= j else 0 for i in range(m)] for j in range(m)]


print(make_lower_triangular_matrix(3))
