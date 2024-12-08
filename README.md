# Библиотечная система управления

## Описание
Это консольное приложение для работы с библиотекой книг. Оно предоставляет функционал для добавления, удаления, поиска и отображения книг. Каждая книга имеет следующие характеристики:
- **id**: уникальный идентификатор (создается автоматически)
- **title**: название книги
- **author**: автор книги
- **year**: год издания
- **status**: статус книги ("в наличии" или "выдана")

---

## Основные функции
1. **Добавление книги**  
   Пользователь вводит название книги, автора и год издания. Программа добавляет книгу с уникальным id и статусом "в наличии".
   
2. **Удаление книги**  
   Позволяет удалить книгу по ее уникальному id.

3. **Поиск книг**  
   Реализован поиск книг по названию, автору или году издания.

4. **Отображение всех книг**  
   Приложение выводит полный список книг с их id, названием, автором, годом издания и текущим статусом.

5. **Изменение статуса книги**  
   Пользователь вводит id книги и изменяет ее статус на "в наличии" или "выдана".

---

## Хранение данных
- Все данные о книгах сохраняются в файл **lib.json** в формате JSON.

---

## Обработка ошибок
Программа поддерживает обработку ошибок, включая:
- Удаление книги с несуществующим id.
- Некорректный ввод данных (например, текст вместо числового id).

---

## Тестирование
Для проверки работы приложения предусмотрены тесты, расположенные в файле **test_library.py**:
- Запуск тестов выполняется командой:  
  ```bash
  python3 test_lib.py

- Тесты охватывают основные сценарии работы программы. При успешном выполнении появится сообщение: **OK**.

---

## Инструкция по использованию

### Как запустить приложение

1. Скачайте или клонируйте репозиторий с проектом.
2. Убедитесь, что Python установлен на вашем компьютере.
3. Для запуска приложения выполните команду: `python3 main.py`.

### Пример работы приложения

После запуска программы на экране появится меню с доступными действиями:

```bash
Система управления библиотекой запущена.

Меню:
1. Добавить книгу
2. Удалить книгу
3. Поиск книги
4. Отображение всех книг
5. Изменение статуса книги
6. Выход
Выберите действие:
```
* Добавление книги: Выберите действие 1, введите название, автора и год издания книги.
* Удаление книги: Выберите действие 2, введите id книги, которую нужно удалить.
* Поиск книги: Выберите действие 3, укажите поле для поиска и запрос.
* Отображение всех книг: Выберите действие 4.
* Изменение статуса книги: Выберите действие 5, укажите id книги и новый статус.
* Выход из приложения: Выберите действие 6.