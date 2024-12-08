import json
import os
from typing import List, Dict


class Library:
    LIBRARY_FILE = 'lib.json'

    def __init__(self):
        self.library = self.load_library()

    def load_library(self) -> List[Dict]:
        if os.path.exists(self.LIBRARY_FILE):
            try:
                with open(self.LIBRARY_FILE, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Ошибка: поврежден файл библиотеки. Загружается пустая библиотека.")
                return []
        return []

    def save_library(self) -> None:
        with open(self.LIBRARY_FILE, 'w', encoding='utf-8') as file:
            json.dump(self.library, file, ensure_ascii=False, indent=4)

    def get_next_id(self) -> int:
        """
        Возвращает следующий доступный id для новой книги.
        """
        if not self.library:
            return 1
        return max(book['id'] for book in self.library) + 1

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Добавляет новую книгу в библиотеку.
        """
        new_book = {
            'id': self.get_next_id(),
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии'
        }
        self.library.append(new_book)
        self.save_library()
        print(f"Книга '{title}' успешно добавлена в библиотеку.")

    def delete_book(self, book_id: int) -> None:
        """
        Удаляет книгу по id.
        """
        book_to_delete = next((book for book in self.library if book['id'] == book_id), None)
        if book_to_delete:
            self.library.remove(book_to_delete)
            self.save_library()
            print(f"Книга с id {book_id} удалена из библиотеки.")
        else:
            print(f"Книга с id {book_id} не найдена.")

    def search_books(self, query: str, field: str) -> List[Dict]:
        """
        Ищет книги по указанному полю.
        """
        valid_fields = ['title', 'author', 'year']
        if field not in valid_fields:
            print(f"Ошибка: Поле '{field}' не поддерживается. Используйте одно из: {', '.join(valid_fields)}.")
            return []
        return [book for book in self.library if query.lower() in str(book[field]).lower()]

    def display_books(self) -> None:
        """
        Отображает список всех книг в библиотеке.
        """
        if self.library:
            print("Список книг:")
            for book in self.library:
                print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                      f"Год: {book['year']}, Статус: {book['status']}")
        else:
            print("В библиотеке нет книг.")

    def update_status(self, book_id: int, status: str) -> None:
        """
        Обновляет статус книги по id.
        """
        if status not in ['в наличии', 'выдана']:
            print("Ошибка: Статус должен быть 'в наличии' или 'выдана'.")
            return
        book_to_update = next((book for book in self.library if book['id'] == book_id), None)
        if book_to_update:
            book_to_update['status'] = status
            self.save_library()
            print(f"Статус книги с id {book_id} обновлен на '{status}'.")
        else:
            print(f"Книга с id {book_id} не найдена.")


def main() -> None:
    library = Library()
    print("Система управления библиотекой запущена.")

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отображение всех книг")
        print("5. Изменение статуса книги")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания книги: "))
                library.add_book(title, author, year)
            except ValueError:
                print("Ошибка: Год издания должен быть числом.")
        elif choice == '2':
            try:
                book_id = int(input("Введите id книги, которую нужно удалить: "))
                library.delete_book(book_id)
            except ValueError:
                print("Ошибка: id книги должен быть числом.")
        elif choice == '3':
            search_field = input("Введите поле для поиска (title, author, year): ").strip()
            search_query = input("Введите запрос для поиска: ").strip()
            found_books = library.search_books(search_query, search_field)
            if found_books:
                print("Найденные книги:")
                for book in found_books:
                    print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                          f"Год: {book['year']}, Статус: {book['status']}")
            else:
                print("Книг по вашему запросу не найдено.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            try:
                book_id = int(input("Введите id книги: "))
                status = input("Введите новый статус (в наличии или выдана): ").strip()
                library.update_status(book_id, status)
            except ValueError:
                print("Ошибка: id книги должен быть числом.")
        elif choice == '6':
            print("Завершение работы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
