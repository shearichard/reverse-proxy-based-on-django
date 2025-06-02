# 

## Summary
Some experiments with [django-revproxy](https://django-revproxy.readthedocs.io/en/latest/index.html) , the repos for the django-revproxy is [here](https://github.com/jazzband/django-revproxy).

## Getting Going
### Run protected app
To run the app which sits behind the proxy, from the root of the project, make the virtualenv active, change the directory to the `protected_app` and run the `prtcd_app.py` module.

```
$ pipenv shell
(django-revproxy-sandbox)$ cd protected_app
(django-revproxy-sandbox)$ python prtcd_app.py 
 * Serving Flask app 'prtcd_app'
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
 
### Run proxy app
To run the app which provides the proxy, from the root of the project, make the virtualenv active, change the directory to the `proxy_app` and then use the Django `runserver` command.

```
$ pipenv shell
(django-revproxy-sandbox)$ cd proxy_app
(django-revproxy-sandbox)$ python manage.py runserver 
Watching for file changes with StatReloader
Performing system checks...
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Using the proxy
Requests made to http://127.0.0.1:8000 will be passed onto the application app sitting behind the proxy, for example ...

```
$ curl  -L http://127.0.0.1:8000/api/v1/country/2
{
  "area_sq_km": 50000,
  "country_iso_code": "USA",
  "id": 2,
  "population": 1000000
}
```

 
## Virtualenv Management
[pipenv](https://pipenv.pypa.io/en/latest/) is in use as the virtualenv management tool.

## Linting
[flake8](https://flake8.pycqa.org/en/latest/) is used for code quality checking.

Be sure to check the .flake8 file for exclusions from the standard rules.

## Code Formatting
The [black](https://black.readthedocs.io/en/stable/) is installed for automatted code formatting, if that's your thing.
