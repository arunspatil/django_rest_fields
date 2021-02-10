from .constants import int_type, invalid_step


def is_list(list_data):
    print('assss')
    return True if type(list_data) is list else False


def is_iterable(list_data):
    iterables = [int, float, str]
    return True if type(list_data) in iterables else False


def create_list():
    list_data = input("enter list items").split()
    return list_data


def list_append(list_data, list_item):
    list_data.append(list_item)
    print(list_data)
    return list_data


def list_extend(list1, list2):
    list1.extend(list2)
    return list1


def list_slicing(list_data, start_index, end_index, step):
    print(start_index, end_index, step)
    return list_data[start_index:end_index:step]


def list_copy(source_list):
    return source_list.copy()


def list_count(list_data):
    return len(list_data)


def list_index(list_data, indexing_item):
    return list_data.index(indexing_item)


def list_insert(list_data, index, item_to_be_inserted):
    list_data.insert(index, item_to_be_inserted)
    return list_data


def list_reverse(list_data):
    list_data.reverse()
    return list_data


def list_sort(list_data):
    list_data.sort()
    return list_data


def list_substraction(left_list1, right_list):
    list3 = list()
    for list_item in left_list1:
        if list_item not in right_list:
            list3.append(list_item)
    return list3


def list_remove(list_data, item_to_be_removed):
    list_data.remove(item_to_be_removed)
    return list_data


def list_clear(list_data):
    list_data.clear()
    return list_data

