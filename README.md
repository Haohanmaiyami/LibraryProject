# 📚 LibraryProject – Django REST API with CI/CD

It’s a training project of an online library built with Django: it manages books, authors and reviews, and has a fully configured Docker + CI/CD pipeline — the code is automatically linted and tested, built into a Docker image, and deployed to a remote server via GitHub Actions.

## What this project does

- Exposes a simple Django REST API for a library (books/authors, admin panel at `/admin/`).
- Runs inside Docker containers (web + database via `docker-compose.yml`).
- Uses **GitHub Actions** to:
  - run `flake8` (lint),
  - run Django tests (`python manage.py test`),
  - build and push a Docker image to **Docker Hub**,
  - deploy to a remote server via SSH and `docker compose`.

## Tech stack

- Python 3.x, Django, Django REST Framework
- PostgreSQL (in Docker), SQLite for tests
- Docker & Docker Compose
- GitHub Actions
- flake8 for linting

## Quick start (Docker, local)

```bash
git clone https://github.com/Haohanmaiyami/LibraryProject.git
cd LibraryProject
cp .env.example .env  # fill in variables
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

App: http://127.0.0.1:8000  
Admin: http://127.0.0.1:8000/admin/

## CI/CD in short

Workflow: `.github/workflows/ci.yml`

On push / pull request:

1. **lint** – flake8
2. **test** – Django tests
3. **build** – build & push Docker image to Docker Hub
4. **deploy** – SSH to server and run `docker compose up -d --build`

Secrets used (examples): `DOCKER_HUB_USERNAME`, `DOCKER_HUB_ACCESS_TOKEN`, `SSH_PRIVATE_KEY`, `SERVER_IP`, `SERVER_USER`, `SECRET_KEY`, DB credentials.

This repo can be used as a compact example of a Django REST project with Docker and a working CI/CD pipeline.


________________________________________________________
____________________________
____________________________
____________________________





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
