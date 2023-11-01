#!/usr/bin/env python3
"""app module
containing simple translation to france or english
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    return the rendered html code used for
    the internationalization
    return a string of the html code
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
