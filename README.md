# newscontent
Новостной сайт. Реализовано:

- Создание новости (поста)

- Разбитие новостей на категории

- Регистрация, авторизация пользователей (формирование токенов при регистрации)

- Модель пользователя


Инструкция

Необходимо установить виртуальное окружение (python -m venv venv)

Активировать его (Windows: .\venv\Scripts\activate, Linux: source venv/Scripts/activate)

Необходимые библиотеки:

pip install django

pip install djangorestframework

pip install Pillow

cd newscontent

Запустить сервер: python manage.py runserver 8000

Пройти по ссылке http://127.0.0.1:8000

Доступ к админке (Логин/пароль: admin / admin) - http://127.0.0.1:8000/admin

В таблице Tokens при регистрации пользователя будут генерироваться токены

Модель находится в приложении users (newscontent/newscontent/users/model.py)

Формы для регистрации (newscontent/newscontent/users/forms.py)

Функции прописаны (newscontent/newscontent/users/views.py)

