# Production Engineering - Week 1 - Portfolio Site

Hey guys! During Week 1, me (Pavlo) & my teammate Yixing were asked to build a portfolio site using Flask. This site will be the foundation for activities we do in future weeks so we tried to make it our own and reflect the mix of our personalities!

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```
>⚠️ Note:
> Some dependencies, such as `cffi==1.15.0`, are not compatible with `Python 3.13+`.
> To avoid installation errors, it's recommended to use `Python 3.9–3.11`.

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

>⚠️ Note:
> To make the map work you will need to get your own API_KEY, configure it accordingly and put it in the 
> .env file and it will look like "API_KEY = XXxxxxXXxxxXXXXXxxxXXxxXXxXXXXxXXxxxXxx".
> You can follow this guide to get the API: https://developers.google.com/maps/documentation/embed/get-api-key

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 
