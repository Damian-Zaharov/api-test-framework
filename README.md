# API Automation Testing Framework (DummyJSON)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?logo=pytest&logoColor=white)
![HTTPX](https://img.shields.io/badge/HTTPX-Client-5A29E4)
![Pydantic](https://img.shields.io/badge/Pydantic-V2-E92063?logo=pydantic&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Report-FF6C37?logo=allure&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)


---

Фреймворк для автоматизации тестирования [DummyJSON API](https://dummyjson.com). Проект демонстрирует навыки построения масштабируемой архитектуры, контейнеризации и настройки CI/CD циклов.

## Live Report
 **Результаты последних тестов всегда доступны здесь:**
[![Tests](https://github.com/damian-zaharov/ui-saucedemo-playwright-test-framework/actions/workflows/run_tests.yml/badge.svg)](https://damian-zaharov.github.io/api-test-framework/)

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
