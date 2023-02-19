'''ЗАДАНИЕ 3
Программа на вход должна принимать файл с каким-то текстом. Пользователь вводит
любую английскую букву. Программа должна считать сколько раз эта буква
встречается в тексте (без учёта регистра). То есть буквы n и N считать
одинаковыми.'''


def counter_letters(letter: str, text_to_look: str) -> int:
    '''prints the number of times the letter encounters in the text'''
    letter_count = text_to_look.lower().count(letter)
    return letter_count


input_letter = input('Please enter a Latin letter: ').lower()


with open('text.txt', 'r') as txt_file:
    count_letters = 0
    for line in txt_file:
        count_letters += counter_letters(input_letter, line)

print(f'Letter "{input_letter}" is found {count_letters} time in the text.')
