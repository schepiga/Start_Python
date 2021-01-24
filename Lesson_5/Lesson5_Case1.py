
with open('text_file.txt', 'w', encoding='utf-8') as f:
    while True:
        user_data = (input('Введите свои данные, для выхода нажмите enter' + '\n'))
        f.write(user_data + '\n')
        if user_data == '':
            break



