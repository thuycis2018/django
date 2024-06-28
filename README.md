# django2024 - Sample REST APIs

## Get Started Using Docker Container

Very first time, build Docker image.
 ```bash
docker-compose up --build
```

When changing codes, don't need to build Docker image again. If changing models, need to remove volume as well.
 ```bash
docker-compose down -v
docker-compose up
```

For documentation, visit: http://localhost:8000/swagger/

## Get Started Without Using Docker Container
1. Initial requirements: install Django Rest framework and Swagger documentation
 ```python
pip install djangorestframework
pip install setuptools
pip install drf-yasg
```

2. Run migration
 ```python
python manage.py makemigrations
python manage.py migrate
```

3. Run dev server
 ```python
python manage.py runserver
```


4. Populate data
 ```python
python manage.py populate_products
```

5. Run tests
 ```python
python manage.py test products
```

6. Code linting
 ```python
flake8
pylint products/
```