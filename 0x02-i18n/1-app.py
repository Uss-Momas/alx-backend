#!/usr/bin/env python3
"""app module"""
from flask import Flask, render_template
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


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    return the rendered page
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
