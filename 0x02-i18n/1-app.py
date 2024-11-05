#!/usr/bin/env python3
"""A basic Flask application with internationalization support.
"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Configuration class for Flask Babel.
    """
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from the Config class
app.url_map.strict_slashes = False  # Allow trailing slashes in routes
babel = Babel(app)  # Initialize Babel for internationalization


@app.route('/')
def get_index() -> str:
    """Render the home/index page.
    """
    return render_template('1-index.html')  # Serve the index HTML template


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the Flask app on host 0.0.0.0 and port 5000
