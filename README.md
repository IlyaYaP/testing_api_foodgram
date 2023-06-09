# Учебный проект по автоматизации тестирования API 
В данном проекте реализована попытка автоматизации тестирования API дипломного проекта [Foodgram(YandexPracticum)](https://github.com/IlyaYaP/foodgram-project-react)
### Стек технологий:
Стек: Python 3.10, Pytest 7.3.1, Allure-pytest 2.13.2, Pydantic 1.10.8
# Развертывание проекта
- Развертываем проект [Foodgram(YandexPracticum)](https://github.com/IlyaYaP/foodgram-project-react) в соответствии с инструкцией.
- Через [Django administration](http://localhost/admin/) создаем 1-2 тестовых пользователя и рецепта.
- После успешного запуска проекта Foodgram клонируем данный репозиторий с проектом:
```
git clone https://github.com/IlyaYaP/testing_api_foodgram.git
```
- В папке с проектом создаем и активируем виртуальное окружение:
```
python -m venv venv
source venv/scripts/activate
```

- Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Запускаем тесты:
```
pytest -s -v --alluredir result_allure --tb=long
```

- Установка allure на Windows.
```
scoop install allure 
```

- Формируем отчет allure.
```
allure serve result_allure
```
- Наслаждаемся красивым отчетом, где можно детально разобрать все тест-кейсы.

После тестов, желательно чистить БД, проще всего это сделать через админку:
```
http://localhost/admin/
```

Документация API доступна по адресу:
```
http://localhost/api/docs/
```
