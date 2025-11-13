## Реализация древовидного меню

### Технологии

- Python3, Django
- PostgreSQL 
- Docker, Docker Compose

### Установка и запуск

Открываем терминал, создаём папку, в которой будет располагаться проект и переходим в неё:
```bash
mkdir /ваш/путь
cd /ваш/путь
```
Клонируем репозотирий в эту папку, переходим в папку проекта:
```bash 
git clone https://github.com/DmitriyChubarov/UpTrader.git
```
```bash 
cd UpTrader/
```
Создаём .env файл
```bash
touch .env
```
```bash
DEBUG=1
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=user
POSTGRES_PASSWORD=up_trader_password
POSTGRES_DB=up_trader_db
```

Запускаем Docker на устройстве, после чего запускаем сервис и создаем суперюзера:
```bash
docker compose up --build
```
```bash
docker compose run --rm web python3 manage.py createsuperuser
```
Заходим в админку и создаём меню
```bash
http://localhost:8000/admin/ - админка
```
После создания меню, в файл test_menu.html добавляем
```bash
{% main_menu 'название Menu из админки' %}
```
Сервисом можно пользоваться
```bash
http://127.0.0.1:8000/tree/
```

### Контакты
- tg: @eeezz_z
- gh: https://github.com/DmitriyChubarov

