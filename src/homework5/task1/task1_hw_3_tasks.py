def fizzbuzz():
    for i in (range(1, 101)):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)


def list_pract():
    correct_list = [a + b for a in "ab" for b in "bcd"]
    correct_list2 = correct_list[::2]
    correct_list3 = [x + 'a' for x in '1234']
    print(correct_list3.pop(1))
    correct_list4 = correct_list3.copy()
    correct_list4.insert(1, '2a')


def tuple_pract():
    new_list = ['a', 'b', 'c']
    new_tuple = tuple(new_list)
    new_tuple1 = ('a', 'b', 'c')
    new_list_1 = list(new_tuple1)
    a, b, c = 'a', 2, 'python'
    new_tuple2 = ([1, 2, 3],)
    for x in new_tuple2:
        for new_list in x:
            print(new_list)
    print('Длина кортежа: ' + str(len(new_tuple2)))


def number_pair():
    in_str = '1 1 1 1'
    in_list = list(in_str)
    in_list = [int(n) for n in in_list if n != ' ']
    index = 0
    for i in range(len(in_list)):
        for j in range(i + 1, len(in_list)):
            if in_list[i] == in_list[j]:
                index = index + 1
    print(index)


def count_elements():
    new_list = [2, 4, 5, 3, 3, 5, 6, 7, 5, 4]
    result_list = []
    for i in new_list:
        if new_list.count(i) == 1:
            result_list.append(i)
    print(result_list)


def transformation_num():
    new_list = [1, 3, 6, 0, 0, 4, 5, 6, 3, 0, 0, 0, 6]
    for i in reversed(range(len(new_list))):
        if new_list[i] == 0:
            new_list.append(new_list.pop(i))
    print(new_list)


def runner(func):
    func