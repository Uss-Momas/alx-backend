#!/usr/bin/env python3
"""app module
containing simple translation to france or english
"""
from flask import Flask, render_template, request
from flask import g
from flask_babel import Babel
import pytz
from typing import Union, Dict

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Class configuration of
    Babel I18n
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


def get_user(user_id: Union[int, None]) -> Union[Dict[str, Union[str, None]],
                                                 None]:
    """
    Get a user from users table
    return:
        - Dictionary containing the user information
        or None
    """
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """
    This method is executed before any other method
    because of the flask app.before_request decorator
    Responsible for setting the global variable of flask to contain user name

    Return None
    """
    user_id = request.args.get("login_as")
    user_id = int(user_id) if user_id else None
    user = get_user(user_id)
    setattr(g, "user", user)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for our supported languages
    The default language selected is EN
    Return:
        - the string of the locale: if locale exist as a query parameter,
        return it also
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    if g.user:
        if g.user.get("locale") in app.config["LANGUAGES"]:
            return g.user.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the best match for timezone of our supported languages
    The default language selected is EN
    Return:
        - the string of the timezone
    """
    timezone = request.args.get("timezone", "").strip()
    if not timezone and g.user:
        timezone = g.user.get("timezone")
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    return the rendered html code used for
    the internationalization
    return a string of the html code
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()
