tup_initial = ('шалаш', 'утру', 'гамак', 'дубак', "мем", 'зигота', 'потоп', 'репер')
palindrom_filter = tuple(filter(lambda x: x[::] == x[::-1], tup_initial))
print(palindrom_filter)
