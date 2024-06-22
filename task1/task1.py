# Перше завдання
# У вас є текстовий файл, який містить інформацію про місячні заробітні плати
# розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника
# та його заробітну плату, які розділені комою без пробілів.


def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = [salary.strip() for salary in file.readlines()]
            result = sum([float(salary.split(",")[1]) for salary in salaries])

            return result, result / len(salaries)

    except FileNotFoundError:
        return 0, 0


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")