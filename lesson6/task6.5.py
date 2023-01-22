def decorator(func):
    def wrapper(*args, **kwargs):
        print('Здесь начальный код декоратора')
        func(*args, **kwargs)
        print('Здесь последующий код декоратора')

    return wrapper

@decorator
def main(a: int | float, b: int | float) -> int | float:
    print(a + b)

main(3.7, 4)
