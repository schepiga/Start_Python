glossary = {'One': 'один',
            'Two': 'два',
            'Three': 'три',
            'Four': 'четыре',
}
print(glossary)
with open('text_4.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    for el in text:
        text = text.replace(text[0], glossary.get(text.split()[0]))
    print(glossary.get(text.split()[2]))

    with open('test.txt', 'w', encoding='utf-8') as n:
        n.write(text)
print(text)