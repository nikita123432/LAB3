import re

# Создаем пустой словарь для хранения информации о предметах и количестве занятий
subjects_dict = {}

try:
    # Открываем файл для чтения
    with open('subjects.txt', 'r', encoding="UTF-8") as file:
        # Читаем каждую строку из файла
        for line in file:
            # Разбиваем строку на части с помощью двоеточия
            parts = line.strip().split(':')
            if len(parts) == 2:
                subject_name = parts[0].strip()  # Название предмета
                details = parts[1].split()  # Детали о количестве занятий

                # Инициализируем счетчик общего количества занятий
                total_lessons = 0

                # Обходим детали о занятиях и суммируем их
                for detail in details:
                    # Используем регулярное выражение, чтобы извлечь число из строки
                    match = re.search(r'(\d+)', detail)
                    if match:
                        lesson_count = int(match.group(1))
                        total_lessons += lesson_count

                # Добавляем информацию в словарь
                subjects_dict[subject_name] = total_lessons

    # Выводим словарь на экран
    print(subjects_dict)

except FileNotFoundError:
    print("Файл не найден.")
