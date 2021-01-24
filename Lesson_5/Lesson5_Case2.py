with open('text.txt', 'r', encoding='utf-8') as f:
    string = f.readlines()
    print(f'В тексте {len(string)} строки')
    print('-' * 25)

    for line, number in enumerate(string):
        total_words = len(number.split())
        print(f'{line+1}-я строка содержит {total_words} слова')

