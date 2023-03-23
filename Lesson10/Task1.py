list_word = ['разработка', 'сокет', 'декоратор']
for i in list_word:
    print(f'{i} - {type(i)}')
print('Строковые представления в формате Unicode')
list_word_t = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442',
               '\u0434\u0435\u043a\u0430\u0440\u0430\u0442\u043e\u0440']
for i in list_word_t:
    print(f'{i} - {type(i)}')