import logging


# Generators, task_1_1:
def even_numb_gen(numb):
    count = 0
    while count < numb + 1:
        if count % 2 == 0:
            yield count
        count += 1

# Закоментив, щоб не заважало.
# if __name__ == "__main__":
#     numb: int = int(input("Вкажіть до якого числа генерувати парні числа?\n"))
#     gen = even_numb_gen(numb)
#     while True:
#         try:
#             print(next(gen))
#         except StopIteration:
#             break


# Generators, task_1_2:
def fib_gen(lim):
    a, b = 0, 1
    while a < lim:
        yield a
        a, b = b, a + b


# Закоментив, щоб не заважало.
# if __name__ == "__main__":
#     lim: int = int(input("Вкажіть до якого числа генерувати числа Фібоначчі?\n"))
#     fib = fib_gen(lim)
#     while True:
#         try:
#             print(next(fib))
#         except StopIteration:
#             break


# Iterators, task_2_1:
class RevIterator:
    def __init__(self, max_num):
        self.current = max_num

    def __iter__(self):
        return self

    def __next__(self):
        c_num = self.current
        if c_num >= 0:
            self.current -= 1
            return c_num
        else:
            raise StopIteration


# Закоментив, щоб не заважало.
# if __name__ == "__main__":
#     lim: int = int(input("Вкажіть з якого числа почати зворотній відлік?\n"))
#     for num in RevIterator(lim):
#         print(num)


# Iterators, task_2_2:
class EvenIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.max_num:
            c_numb = self.current
            self.current += 1
            if c_numb % 2 == 0:
                return c_numb
        raise StopIteration


# if __name__ == "__main__":
#     lim: int = int(input("Вкажіть до якого числа ітерувати парні числа?\n"))
#     for num in EvenIterator(lim):
#         print(num)


# Decorators, task_3_1:
def attr_res_logger_decor(func):
    logging.basicConfig(
        filename='fib_logs.txt',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True)
    logger = logging.getLogger("attr_res_logger_decor")

    def wrapper(*args, **kwargs):
        logger.info(f"Виклик функції {func.__name__} з аргументами: args = {args} або kwargs = {kwargs}.")
        res = func(*args, **kwargs)
        logger.info(f"Функція {func.__name__} повернула значення: {res}.")
        return res
    return wrapper


@attr_res_logger_decor
def fib_gen_l(lim):
    a, b = 0, 1
    while a < lim:
        yield a
        a, b = b, a + b


# Закоментив, щоб не заважало.
if __name__ == "__main__":
    for numb in fib_gen_l(40):
        print(f"Число Фібоначчі: {numb}")


# Decorators, task_3_2:
def skip_err_decor(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            print(f"Виникла помилка: {exc}")
    return wrapper


@skip_err_decor
def sum_func(data):
        return sum(list(map(int, data.split(","))))


# if __name__ == "__main__":
#     entry_data = ["1,2,3,4", "1,2,3,4,50", 123, "34,2,7,13", True, "qwerty1,2,3", "1,2,3,4,50"]
#     for i in entry_data:
#         print(sum_func(i))
