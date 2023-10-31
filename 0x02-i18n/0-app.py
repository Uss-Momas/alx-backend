#!/usr/bin/env python3
"""app module"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index() -> str:
    """first route defined
    Return a render_template string of the html file
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
