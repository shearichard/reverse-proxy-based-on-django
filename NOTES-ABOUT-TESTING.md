** This entire README is a copy of one used in another repos of mine, django-testing-example. It's just here for ease of reference but some of it isn't relevant. **
# Django Testing Examples

### Test this repository
```bash
git clone https://github.com/ptrstn/django-testing-examples.git
cd django-testing-examples
python -m venv venv
source venv/bin/activate
pip install django==1.11
pip install -r testing-requirements.txt
pytest
```

### Generate HTML coverage report
```bash
pytest --cov=. --cov-report=html
chromium htmlcov/index.html
```

### Test for Deprecation Warnings
If you want to upgrade from Django 1.11 to Django 2.0 you need to make sure that there are no DeprecationWarnings:
```bash
PYTHONWARNINGS=all pytest
# or
python -Wall manage.py test
```

### Test with PyCharm
 - do "Test this repository" steps then open folder with PyCharm

 - File -> Settings -> Tools -> Python Integrated tools ->
Default test runner: py.test -> OK

 - Run -> Run... ->  Edit Configuratinos... -> + -> Python tests -> py.test -> Name: pytest -> OK

 - Run -> 'pytest'

### How this project was created
```bash
mkdir django-testing-examples
cd django-testing-examples
python -m venv venv
source venv/bin/activate
pip install -I django==1.11
git init
wget "https://www.gitignore.io/api/django%2Cpython%2Cpycharm%2Ball" -O .gitignore
django-admin startproject django_testing_examples .
python manage.py startapp myapp
python manage.py migrate
```

# Resources

The Django Test Driven Development Cookbook:
- https://www.youtube.com/watch?v=41ek3VNx_6Q
