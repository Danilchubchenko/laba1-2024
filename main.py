from typing import Optional

from infra import JSONRepository
from entity import Document


def clear_screen():
    """Очищает экран консоли."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt: str) -> Optional[str]:
    """Получает ввод пользователя с обработкой ошибок."""
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input.strip()
        print("Ввод не может быть пустым. Попробуйте снова.")

def display_menu():
    """Отображает главное меню."""
    clear_screen()
    print("Меню:")
    print("1. Добавить файл")
    print("2. Чтение файла")
    print("7. Выход") 

def main():
    while True:
        display_menu()
        choice = get_user_input("Выберите пункт меню: ")
        try:
            if choice == "1":
                filename = get_user_input("Введите название файла ")
                doc = Document(filename, content="")
                content = {"data": get_user_input("Введите содержимое файла ")}
                doc.content = content
                repo = JSONRepository(doc.filename)
                repo.save_data(data=doc.content)
                print("Файл успешно добавлен")
                input("Нажмите Enter, чтобы продолжить...")

            elif choice == "2":
                filename = get_user_input("Название файла: ")
                doc = Document(filename, "")
                repo = JSONRepository(doc.filename)
                print(f"Содержимое файла:\n{repo.load_data()['data']}")
                input("Нажмите Enter, чтобы продолжить...")


            elif choice == "7":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
            input("Нажмите Enter, чтобы продолжить...")
if __name__ == "__main__":
    main()