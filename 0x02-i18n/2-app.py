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
app.config.from_object(Config)  # Load configuration from the Config class
app.url_map.strict_slashes = False  # Allow both trailing and non-trailing slashes in URLs
babel = Babel(app)  # Initialize Babel for localization and internationalization


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for the user's preferred language.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])  # Selects the best language based on client preferences


@app.route('/')
def get_index() -> str:
    """Render the home/index page.
    """
    return render_template('2-index.html')  # Serve the index HTML template


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the Flask app on host 0.0.0.0 and port 5000
