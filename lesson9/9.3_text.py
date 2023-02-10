'''ЗАДАНИЕ 3
Программа на вход должна принимать файл с каким-то текстом. Пользователь вводит
любую английскую букву. Программа должна считать сколько раз эта буква
встречается в тексте (без учёта регистра). То есть буквы n и N считать
одинаковыми.'''

with open('text.txt', 'r') as txt_file:
    text = txt_file.read()

input_letter = input('Please enter a Latin letter: ').lower()


def counter_letters(letter: str, text_to_look: str) -> None:
    '''prints the number of times the letter encounters in the text'''
    letter_count = text_to_look.lower().count(letter)
    print(f'Letter "{letter}" is found {letter_count} in the text.')


counter_letters(input_letter, text)
