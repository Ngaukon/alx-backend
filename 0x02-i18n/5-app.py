#!/usr/bin/env python3
"""A basic Flask application with internationalization support.
"""
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


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
users = {  # Sample user data with their corresponding locales and timezones
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on the 'login_as' query parameter.
    Returns the user data if found, otherwise returns None.
    """
    login_id = request.args.get('login_as')  # Get the 'login_as' parameter from the query string
    if login_id:
        return users.get(int(login_id))  # Retrieve the user based on the provided ID
    return None  # No user found


@app.before_request
def before_request() -> None:
    """Prepares the user data before processing each request.
    Sets the global user variable for use in the request context.
    """
    user = get_user()  # Retrieve user information
    g.user = user  # Store user data in the global object for later access


@babel.localeselector
def get_locale() -> str:
    """Selects the appropriate locale for the web page.
    Checks for a 'locale' query parameter, falling back to the best match
    from the client's accepted languages if not provided.
    """
    locale = request.args.get('locale', '')  # Get the 'locale' parameter from the query string
    if locale in app.config["LANGUAGES"]:  # Validate the provided locale
        return locale  # Return the specified locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])  # Fallback to the best match


@app.route('/')
def get_index() -> str:
    """Render the home/index page.
    """
    return render_template('5-index.html')  # Serve the HTML template for the index page


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the Flask app on all available interfaces at port 5000
