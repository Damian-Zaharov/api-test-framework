# API Automation Testing Framework (DummyJSON)

Профессиональный фреймворк для автоматизации тестирования [DummyJSON API](https://dummyjson.com). Проект демонстрирует навыки построения масштабируемой архитектуры, контейнеризации и настройки CI/CD циклов.

## Live Report
 **Результаты последних тестов всегда доступны здесь:** [Allure Report on GitHub Pages](https://github.io)

## Стек технологий
* **Python 3.11+**
* **Pytest** — тестовый движок.
* **HTTPX** — современный асинхронный HTTP-клиент.
* **Pydantic V2** — строгая валидация схем данных.
* **Allure Reports** — интерактивные отчеты с визуализацией шагов.
* **Docker & Docker Compose** — контейнеризация тестов для изолированного запуска.
* **GitHub Actions** — автоматический запуск тестов и деплой отчетов (CI/CD).

## Архитектура проекта
Проект построен по принципу многослойности (Layered Architecture):
* `core/` — базовый HTTP-клиент с логированием и механизмом Retries.
* `clients/` — описание эндпоинтов API.
* `services/` — бизнес-логика: управление сессиями, токенами и сборка сценариев.
* `schemas/` — Pydantic-модели для автоматической валидации JSON-ответов.
* `utils/` — вспомогательные инструменты: валидаторы и декораторы.
* `tests/` — тестовые сценарии, разделенные по функциональным модулям.

## Варианты запуска

### 1. Локальный запуск (Python)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate | Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest --alluredir=allure-results
allure serve allure-results
```

### 2. Запуск в Docker (Изолированная среда)
```bash
docker-compose build
docker-compose up
```
*Результаты тестов автоматически синхронизируются с папкой `allure-results` на хосте.*

## CI/CD Pipeline
В проекте настроен GitHub Actions (`tests.yml`), который при каждом пуше:
1. Поднимает окружение и устанавливает зависимости.
2. Запускает весь набор тестов.
3. Генерирует и публикует актуальный Allure-отчет в ветку `gh-pages`.

## Покрытие тестами
* **Auth**: Positive/Negative login, Profile data.
* **Products**: CRUD операции (Create, Read, Update, Delete), поиск с параметризацией.

## Визуализация отчетов
![Dashboard](screenshots/main_report.png)
*Общий статус прохождения тестов*

![Test Details](screenshots/test_details.png)
*Детализация шагов и логирование запросов*
