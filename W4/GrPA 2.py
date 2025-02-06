# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <noloop>")[2]
if "for " in content or "while " in content:
    print("You should not use for loop, while loop or the word for and while anywhere in this exercise")

# note that apart from the print statements inside the functions, the evaluator will also print what is returned by the function at last
# <noloop>

def list_mutating_operations(items:list, item1, item2):
    # sort the `items` inplace
    items.sort()
    print("sorted:",items)

    # add item1 to the `items` at the end
    items.append(item1)
    print("append:",items)

    # add item2 at index 3
    items.insert(3, item2)
    print("insert:",items)

    # extend `items` with the first three elements in `items`
    items.extend(items[:3])
    print("extend:", items)

    # pop the fifth element and store it in variable `popped_item`
    popped_item = items.pop(4)
    print("pop:",items)

    # remove first occurance of `item2` from the list
    items.remove(item2)
    print("remove:",items)

    # make the element at index 4 None
    items[4] = None
    print("modify_index:",items)

    # make the even indices None
    items[0::2] = [None] * int(len(items)/2) if len(items)%2 == 0 else [None] * int(len(items)/2 + 1)
    print("modify_slice:",items)

    # delete the third last element
    items.pop(-3)
    print("delete_index:",items)

    # delete the even indices
    del items[0::2]
    print("delete_slice:",items)

    return items, popped_item 

def list_non_mutating_operations(items:list, item1, item2):

    # print the sorted version of items
    print("sorted:", sorted(items))

    # print a lsit with item1 appended to the `items` at the end
    lsit = items + [item1]
    print("append:", lsit)

    # print a list with item2 added to items at index 3
    lsinsert = list(items)
    lsinsert.insert(3, item2)
    print("insert:", lsinsert)

    # print a list with the first three elements in `items` added to the end of the `items` again
    # lsextend = 
    print("extend:", items + items[0:3])

    #  print a list with the fifth element from `items` removed
    print("pop:",items[0:4] + items[5:])

    # print a list with first occurance of `item2` removed from `items` 
    lsrm = list(items)
    lsrm.remove(item2)

    print("remove:", lsrm) # hint: you may want to use index

    # print a list with the fourth element of `items` changed to None
    mils = list(items)
    mils[3] = None
    print("modify_index:", mils)

    # print a list with the even indices changed to None
    msls = list(items)
    msls[::2] = [None] * len(msls[::2])
    print("modify_slice:", msls)

    # print a list with the even indices removed
    dsls = list(items)
    del dsls[::2]
    print("delete_slice:", items[1::2])

    return items

def do_set_operation(set1, set2, set3, item1, item2):
    # add item1 to set1
    set1.add(item1)
    print(sorted(set1))
    # remove item2 from set1. What if item2 is not in set1?
    set1.discard(item2)
    print(sorted(set1))

    # add elements from set2 to set1
    set1.update(set2)
    print(sorted(set1))

    # remove all elements from set1 that are in set3
    set1.difference_update(set3)
    print(sorted(set1))

    # print the common elements in both set2 and set3 as a sorted list.
    print(sorted(set2 & set3))

    # print all unique elements present in set1, set2 an set3 as a sorted list
    print(sorted(set1 | set2 | set3))

    # print all unique elements that are in set2 but not in set3 as a sorted list
    print(sorted(set2 - set3))

    # print all the non common elements from both set2 and set3
    print(sorted(set2 ^ set3))

    return set1,sorted(set1),sorted(set2),sorted(set3)
