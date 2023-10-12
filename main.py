# Создаем и записываем данные в файл F1
with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку (пустая строка для завершения): ")
        if not line:
            break
        f1.write(line + '\n')

# Копируем строки с двумя одинаковыми словами в файл F2
with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    for line in f1:
        words = line.split()
        for word in words:
            if words.count(word) == 2:
                f2.write(line)
                break

# Определяем номер слова с наибольшим количеством букв "А"
with open('F1.txt', 'r') as f1:
    words = f1.read().split()
    max_a_count = 0
    word_with_max_a = None
    for i, word in enumerate(words):
        a_count = word.count('А') + word.count('а')
        if a_count > max_a_count:
            max_a_count = a_count
            word_with_max_a = word
            word_index = i

    if word_with_max_a:
        print(f"Слово с наибольшим количеством букв 'А' - '{word_with_max_a}' (в слове {word_index + 1}).")
    else:
        print("В тексте нет слов с буквой 'А'.")