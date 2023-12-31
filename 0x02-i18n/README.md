# i18n

## Resources
1. [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
2. [pytz](https://pytz.sourceforge.net/)

## Learning Objectives
* Learn how to parametrize Flask templates to display different languages
* Learn how to infer the correct locale based on URL parameters, user settings or request headers
* Learn how to localize timestamps

## Requirements
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5)
* The first line of all your files should be exactly #!/usr/bin/env python3
* All your *.py files should be executable
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions and methods should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

## Installing
1. pip3 install flask_babel==2.0.0

### Flask Babel documenation
1. [Documentation](https://python-babel.github.io/flask-babel/)

#### Babel parametrize templates
1. create Babel config file **babel.cfg** containg
```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

2. Initialize translations with:
```
$ pybabel extract -F babel.cfg -o messages.pot .
```

And 2 dictionaires

```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```

3. Edit the files in **translations/[en|fr]/LC_MESSAGES/messages.po** to provide correct key,value
Use the following example:
| msgid | English | French |
|:-----:|:-------:|:------:|
|home_title| "Welcome to Holberton"	|"Bienvenue chez Holberton"|
|home_header| "Welcome to Holberton" |"Bonjour monde!"|

4. Compile the dictionaires
```
$ pybabel compile -d translations
```