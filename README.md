# e1-homework
[![Travis][build-badge]][build]

[build-badge]: https://img.shields.io/travis/daniltarasov/e1-homework/master.png?style=flat-square

[build]: https://travis-ci.org/daniltarasov/e1-homework

1. Выполнить: git clone https://github.com/daniltarasov/e1-homework.git
2. cd e1-homework
3. Cоздать виртуальное окружение python -m venv venv , активировать.
3. pip install -r requirements.txt
4. Установить PYTHONPATH: export PYTHONPATH=${PWD} (Linux) или set PYTHONPATH=%PYTHONPATH%;<текущий каталог> (windows)
5. Запустить тесты:  pytest --cov=. tests/test_pytest.py
