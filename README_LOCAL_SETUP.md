## Запуск проекта

### Скопировать репозиторий
```bash
git clone https://github.com/MRRomenin/DDS.git
```   
```bash
cd DDS
```    
---
### Установить виртуальное окружение
```bash
python3 -m venv .venv
```
---
### Активация виртуального окружения через:

#### PowerShell
```bash
.\.venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt)
```bash
.venv\Scripts\activate.bat
```

#### Linux / macOS
```bash
source .venv/bin/activate
```
---

### Установка зависимостей

```bash
pip install -r requirements.txt
```
---
### Настройка базы данных и переменных окружения
Создайте пустую базу данных в PostgreSQL.
Скопируйте шаблон .env_example в .env и укажите актуальные параметры подключения к вашей локальной БД (включая DB_HOST=localhost):
```bash
cp .env_example .env
```

### Применение миграций и запуск сервера

```bash
python manage.py migrate
python manage.py runserver
```
После запуска сервис будет доступен по адресу: `http://localhost:8000`


[← Вернуться на главную](README.md)