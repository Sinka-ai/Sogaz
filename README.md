# Приложение для обмена сообщениями на Flask
## Обзор : Приложение написано на Flask, реализована возможность пользователю логиниться, регистрироваться, писать сообщения и создавать чаты. 

## Стек технологий :

- Flask 
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Login 
- PostgreSQL 
- Pandas и Matplotlib 
- Seaborn

<details><summary><b>Установка</b></summary>

1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/yourusername/flask-messenger-app.git
    cd flask-messenger-app
    ```

2. **Создайте виртуальное окружение**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Настройте переменные окружения**:
    Создайте файл `.env` и укажите следующие переменные:
    ```bash
    DATABASE_URL=postgresql://username:password@localhost:5432/yourdatabase
    SECRET_KEY=your_secret_key
    ```

5. **Запустите приложение**:
    ```bash
    flask run
    ```

</details>

<details><summary><b>Скриншоты:</b></summary>
| ![Main page](/pictures/1.png "Main page") | | :--: | | *Main page* |
| ![Login page](/pictures/2.png "Login page") | | *Login page* | 
</details>

<details>
  ```
  <summary><b>Структура проекта</b></summary>
 
  ```
  Sogaz_messenger/
  ├── app/
  │   ├── templates/
  │   │   ├── analytics.html
  │   │   ├── base.html
  │   │   ├── chat.html
  │   │   ├── index.html
  │   │   ├── login.html
  │   │   ├── messages.html
  │   │   ├── register.html
  │   │   └── send_message.html
  │   ├── __init__.py
  │   ├── forms.py
  │   ├── models.py
  │   └── routes.py
  ├── migrations/
  ├── venv/   # Виртуальное окружение
  ├── .gitignore
  ├── config.py
  └── messenger.py
  
 ```
</details>
