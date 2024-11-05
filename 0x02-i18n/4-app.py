#!/usr/bin/env python3
"""A basic Flask application with internationalization support.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Configuration class for Flask Babel settings.
    """
    LANGUAGES = ["en", "fr"]  # Supported languages for translation
    BABEL_DEFAULT_LOCALE = "en"  # Default locale for the application
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone for the application


app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from the Config class
app.url_map.strict_slashes = False  # Allow URLs with or without trailing slashes
babel = Babel(app)  # Initialize Babel for localization


@babel.localeselector
def get_locale() -> str:
    """Selects the appropriate locale for the webpage.
    Checks for a 'locale' query parameter, falling back to the best match
    from the client's accepted languages if not present.
    """
    queries = request.query_string.decode('utf-8').split('&')  # Decode and split the query string
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),  # Create key-value pairs
        queries,
    ))
    if 'locale' in query_table:  # Check if 'locale' parameter exists
        if query_table['locale'] in app.config["LANGUAGES"]:  # Validate the locale
            return query_table['locale']  # Return the specified locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])  # Fallback to the best match


@app.route('/')
def get_index() -> str:
    """Render the home/index page.
    """
    return render_template('4-index.html')  # Serve the HTML template for the index page


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the Flask app on all available interfaces at port 5000
