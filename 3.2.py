# Путь к файлу, учтите правильную кодировку для кириллических символов
filename = "prices.txt"

# Инициализируем общую стоимость заказа
total_cost = 0

try:
    # Открываем файл и читаем его построчно
    with open(filename, "r") as file:
        for line in file:
            
            # Разделяем строку на части по пробелам
            parts = line.split()

            # Проверяем, что в строке есть три части: название, количество и стоимость за единицу
            if len(parts) == 3:
                name = parts[0]
                quantity = int(parts[1])
                unit_price = float(parts[2])

                # Вычисляем стоимость для данной строки и добавляем ее к общей стоимости заказа
                line_cost = quantity * unit_price
                total_cost += line_cost
            else:
                print(f"Ошибка в строке: {line}")

    # Выводим общую стоимость заказа

    print(f"Общая стоимость заказа: {total_cost} рублей")
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
