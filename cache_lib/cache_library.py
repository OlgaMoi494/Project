import time

cache_dct = {}


class SimpleCache:
    def __init__(self, cache_dct=cache_dct):
        self.cache_dct = cache_dct

    def add_element(self, key, value):
        self.cache_dct.setdefault(key, (value, time.time()))

    def cache_by_key(self, key):
        return self.cache_dct.get(key)[0]


class FIFOCache(SimpleCache):

    def __init__(self, max_size, cache_dct=cache_dct):
        super().__init__(cache_dct)
        self.max_size = max_size

    def add_element(self, key, value):
        super().add_element(key, value)
        if len(self.cache_dct) > self.max_size:
            earliest_time = min(
                [value[1] for value in self.cache_dct.values()])
            temp_dct = {}
            for key, value in self.cache_dct.items():
                if value[1] != earliest_time:
                    temp_dct[key] = value
            self.cache_dct = temp_dct


class LRUCache(FIFOCache):
    def __init__(self, max_size, cache_dct=cache_dct):
        super().__init__(max_size, cache_dct)

    def cache_by_key(self, key):
        for k, v in self.cache_dct.items():
            if k == key:
                self.cache_dct[k] = (v, time.time())
        super().cache_by_key(key)


class TTLCache(LRUCache):
    def __init__(self, max_size, ttl_sec, cache_dct=cache_dct):
        super().__init__(max_size, cache_dct)
        self.ttl = ttl_sec

    def add_element(self, key, value):
        super().add_element(key, value)
        temp_dct = {}
        time_now = time.time()
        for key, value in self.cache_dct.items():
            expire_time = value[1] + self.ttl
            if expire_time > time_now:
                temp_dct[key] = value
        self.cache_dct = temp_dct


def cached(cache=SimpleCache()):
    def inner(func):
        def wrapper(*args, **kwargs):
            print(f'args[0] {args[0]}')
            print(cache.cache_dct)
            if args[0] in cache.cache_dct.keys():
                print("Here are cache data.")
                print(cache.cache_by_key(args[0]))
                return cache.cache_by_key(args[0])
            else:
                cache.add_element(args[0], func(*args, **kwargs))
                return func(*args, **kwargs)
        return wrapper
    return inner


@cached(LRUCache(2))
def test(a):
    return a * 2


print(test(2))
print(test(3))
print(test(4))
print(test(4))
