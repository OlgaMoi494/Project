two_words = "жизнь прекрасна"
index_whitespace = two_words.find(' ')
print('!{second_word} ! {first_word}!'.format(
    second_word=two_words[index_whitespace+1:], first_word=two_words[:index_whitespace]))

print(f'!{two_words[index_whitespace+1:]} ! {two_words[:index_whitespace]}!')