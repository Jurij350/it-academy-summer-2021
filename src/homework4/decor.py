import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


def paused(pause):
    def parametrized_paused(func):
        def wrapper(*args, **kwargs):
            print("Start pause")
            time.sleep(pause)
            result = func(*args, **kwargs)
            print("End pause")
            return result

        return wrapper

    return parametrized_paused


@my_decorator
@paused(4)
def func(x, y):
    return x + y


print(func(101, 101))


def my_decor(func):
    count = 0
    def wrapper( *args, **kwargs):
        nonlocal count
        count = count+1
        result = func()
        return result
    return wrapper

def func(index):
    index = index+1
    return index
