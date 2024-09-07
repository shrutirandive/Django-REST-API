# Django REST Framework CRUD & Search API

This project is a simple API built with Django Rest Framework that demonstrates how to create, read, update, delete (CRUD), and search for data through RESTful endpoints. The project can be used as a starting point for understanding how to implement CRUD functionality and basic search capabilities using Django and DRF. It is simple and can be extended further for more complex use cases.

## Features:

Create new records using the ``` /add ``` endpoint

Read existing records from the ``` / ``` endpoint

Update records by providing the ID at ``` /update/<id> ```

Delete records by ID using ``` /delete/<id> ```

Search records by keyword via ``` /search/?search=<keyword> ```

## Technologies:

Django: Python web framework used for rapid development.

Django Rest Framework (DRF): Toolkit to build Web APIs in Django.

SQLite: Default database used for simplicity.


## Run the project 
`python manage.py runserver`

http://127.0.0.1:8000/ ---READ

http://127.0.0.1:8000/add ---CREATE

http://127.0.0.1:8000/update/id ---UPDATE

http://127.0.0.1:8000/delete/id ---DELETE

http://127.0.0.1:8000/search/?search=united ---SEARCH


## Using Postman

You can also perform the same operations using Postman by sending requests to the specified URLs.

![image](https://user-images.githubusercontent.com/54211989/129901795-0ad45cc5-5bfe-4488-8839-6b3534f2e201.png)
![image](https://user-images.githubusercontent.com/54211989/129901968-4fe9a27e-af31-4e66-9822-49bf7ac9a758.png)
Search-->
![image](https://user-images.githubusercontent.com/54211989/129901718-70bc9e04-5f3f-40cd-8adf-16649f0f271e.png)

