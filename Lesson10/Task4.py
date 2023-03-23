list_word = ['разработка', 'администрирование', 'protocol', 'standard']
list_word_b = [i.encode() for i in list_word]
print(f'Байтовое представление {list_word_b}')
list_word_s = [i.decode() for i in list_word_b]
print(f'Строковое представление {list_word_s}')