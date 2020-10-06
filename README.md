## Getting Started

Just clone repository : 
```
https://github.com/rusalforever/test-order.git
```
Go to repository : 
```
cd test-order
```
### Prerequisites and Installing

First of all,  create new environment:
```
python3 -m venv env
```
Activate the new environment:
```
source env/bin/activate
```
Install all requirements: 
```
pip3 install -r requirements.txt
```                                 
DB: 
```
python manage.py migrate
```                                 
Load Products: 
```
python manage.py loaddata product.json
```                                 
Admin Panel: 
```
python manage.py migrate
```                                 
Run tests: 
```
python3 manage.py test
```                                 
Run Server: 
```
python manage.py runserver
```                                 
### API doc
[Swagger](http://127.0.0.1:8000/)
