# Sample REST APIs

## Using Docker container

Build Docker image and run container
 ```sh
docker-compose up --build
```

When changing codes, don't need to build Docker image again. If changing models, need to remove volume as well.
 ```sh
docker-compose down -v
docker-compose up
```

For documentation, visit: http://localhost:8000/swagger/


## Get started without using Docker container
1. Initial requirements: install Django Rest framework and Swagger documentation
 ```sh
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

## APIs
1. GET /api/products/
2. POST /api/products/bulk-create/
3. DELETE /api/products/bulk-delete/
4. PUT /api/products/bulk-update/
5. GET /api/products/{product-id}/
  
