#!/usr/bin/env python3
"""A basic Flask application with internationalization support.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Configuration class for Flask Babel settings.
    """
    LANGUAGES = ["en", "fr"]  # Supported languages for translation
    BABEL_DEFAULT_LOCALE = "en"  # Default language for the application
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone for the application


app = Flask(__name__)
app.config.from_object(Config)  # Load the configuration from the Config class
app.url_map.strict_slashes = False  # Allow URLs with or without trailing slashes
babel = Babel(app)  # Initialize Babel for localization and internationalization


@babel.localeselector
def get_locale() -> str:
    """Selects the best matching locale for the user.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])  # Returns the preferred language based on client settings


@app.route('/')
def get_index() -> str:
    """Render the home/index page.
    """
    return render_template('3-index.html')  # Serve the HTML template for the index page


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the Flask app on all available interfaces at port 5000
