from random import randint

def count_nums(lst: list) -> dict:
    """ Подсчитывает количество повторений каждого элемента во входящем списке"""
    dct_count_nums = {}
    for i in lst:
        if dct_count_nums.get(i) is None:
            dct_count_nums[i] = 1
        else:
            dct_count_nums[i] += 1

    return dct_count_nums


num_lst = [randint(1, 10) for _ in range(20)]
print(num_lst)
print(count_nums(num_lst))

for k, v in count_nums(num_lst).items():
    print(f'Число {k} в списке повторяется {v} раз(а).')
