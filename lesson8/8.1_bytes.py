"""1. Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем
результат преобразовать в байтовый вид в кодировке ‘Latin1’ и затем результат
снова декодировать в строку (результаты всех преобразований выводить на экран)."""

byte_string = b'r\xc3\xa9sum\xc3\xa9'
print(byte_string)
byte_string_decoded = byte_string.decode('utf-8')
print(byte_string_decoded)
str_encode_latin1 = byte_string_decoded.encode('Latin1')
print(str_encode_latin1)
latin1_decode_str = str_encode_latin1.decode('Latin1')
print(latin1_decode_str)
