# YaCut - Сервис укорачивания ссылок

## Описание проекта

YaCut — это сервис для создания коротких ссылок. Он позволяет пользователям ассоциировать длинные URL-адреса с короткими, которые можно легко делиться. Сервис предоставляет возможность как автоматической генерации коротких ссылок, так и использования пользовательских вариантов.

## Установка и настройка

1. **Клонирование репозитория:**
   ```bash
   git clone https://github.com/yourusername/yacut.git
   cd yacut
   ```

2. **Создание и активация виртуального окружения:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate     # Для Windows
   ```

3. **Установка зависимостей:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройка переменных окружения:**
   Создайте файл `.env` в корневой директории проекта и добавьте в него следующие переменные:
   ```env
   DATABASE_URI=sqlite:///yacut.db
   FLASK_APP=yacut
   FLASK_ENV=development
   ```

5. **Инициализация базы данных:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Запуск сервера:**
   ```bash
   flask run
   ```

## Использование

### Веб-интерфейс

После запуска сервера откройте браузер и перейдите по адресу `http://localhost:5000`. Вы увидите главную страницу с формой для создания коротких ссылок.

### API

API сервиса доступен по следующим эндпоинтам:

- **Создание короткой ссылки:**
  - Метод: `POST`
  - URL: `/api/id/`
  - Тело запроса:
    ```json
    {
      "url": "https://example.com",
      "custom_id": "optional_custom_id"
    }
    ```
  - Ответ:
    ```json
    {
      "url": "https://example.com",
      "short_link": "http://yacut.ru/optional_custom_id"
    }
    ```

- **Получение оригинальной ссылки:**
  - Метод: `GET`
  - URL: `/api/id/<short_id>/`
  - Ответ:
    ```json
    {
      "url": "https://example.com"
    }
    ```

### Примеры запросов

1. **Создание короткой ссылки:**
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com", "custom_id": "example"}' http://localhost:5000/api/id/
   ```

2. **Получение оригинальной ссылки:**
   ```bash
   curl http://localhost:5000/api/id/example/
   ```

## Структура проекта

- **`yacut/`** - Основной пакет приложения.
  - **`__init__.py`** - Инициализация приложения.
  - **`models.py`** - Модели базы данных.
  - **`forms.py`** - Формы для веб-интерфейса.
  - **`views.py`** - View-функции для веб-интерфейса.
  - **`api_views.py`** - API-функции.
  - **`templates/`** - Шаблоны для веб-интерфейса.
  - **`static/`** - Статические файлы (CSS, JS).
- **`migrations/`** - Миграции базы данных.
- **`tests/`** - Тесты.
- **`requirements.txt`** - Список зависимостей.
- **`.env`** - Переменные окружения.

## Тестирование

Для запуска тестов выполните команду:
```bash
pytest
```

## Автор

Богданов Дмитрий

## Лицензия

Этот проект лицензирован под MIT License.