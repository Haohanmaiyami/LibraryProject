# LibraryProject

Домашнее задание по настройке CI/CD для Django-приложения.

## Что сделано
- Подготовлен удалённый сервер для деплоя (Docker, SSH-ключи, открытый порт 80).
- Добавлен workflow GitHub Actions `.github/workflows/ci.yml`.
- Настроены шаги:
  - **lint** — проверка кода flake8  
  - **test** — запуск Django тестов на sqlite  
  - **build** — сборка и публикация Docker-образа в Docker Hub  
  - **deploy** — автоматический деплой на сервер после успешных тестов  

## Переменные окружения
Чувствительные данные вынесены в GitHub Secrets:
- `DOCKER_HUB_USERNAME`  
- `DOCKER_HUB_ACCESS_TOKEN`  
- `SSH_KEY`  
- `SSH_USER`  
- `SERVER_IP`

В репозитории есть пример файла `.env.sample`.

## Настройка удаленного сервера и его деплой

1. Установить на сервере Docker и Docker Compose.
2. Открыть порт **80** (или нужный для приложения).
3. Настроить доступ по SSH-ключу (ключ добавлен в `~/.ssh/authorized_keys`).
4. Создать на сервере файл `.env` по образцу `.env.sample`.
5. GitHub Actions автоматически:
   - прогоняет тесты,
   - собирает и пушит Docker-образ в Docker Hub,
   - деплоит контейнер на сервер.
6. Для запуска вручную на сервере:
   ```bash
   docker pull <DOCKER_HUB_USERNAME>/myapp:<TAG>
   docker run -d --name myapp -p 80:8000 <DOCKER_HUB_USERNAME>/myapp:<TAG>
   


Приложение доступно по IP, при обращении к корню возвращается 404, но рабочие эндпоинты доступны (например, /admin/)


------------------------

# Курс 9 Итоговое задание

Учебный проект на Django Rest Framework с Docker Compose и CI/CD.

## Локальный запуск
```bash
git clone https://github.com/Haohanmaiyami/LibraryProject.git
cd LibraryProject
cp .env.example .env   # заполнить переменные
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Приложение: http://127.0.0.1:8000

## Сервер
Развёрнутый проект доступен по адресу:
 http://84.252.139.98

## CI/CD
Линтер flake8 и тесты python manage.py test

Сборка и пуш Docker-образа в Docker Hub

Автодеплой на сервер через docker compose up -d --build

GitHub Secrets
DOCKER_HUB_USERNAME, DOCKER_HUB_ACCESS_TOKEN,
SSH_PRIVATE_KEY, SERVER_IP, SERVER_USER,
SECRET_KEY, DB_NAME, DB_USER, DB_PASSWORD

.................
----------------
