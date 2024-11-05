#!/usr/bin/env python3
"""A basic Flask application with internationalization support.
"""
import pytz
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Configuration class for Flask Babel settings.
    """
    LANGUAGES = ["en", "fr"]  # Supported languages for the application
    BABEL_DEFAULT_LOCALE = "en"  # Default locale to be used for translations
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone for the application


app = Flask(__name__)
app.config.from_object(Config)  # Load configuration settings from the Config class
app.url_map.strict_slashes = False  # Allow both trailing and non-trailing slashes in URLs
babel = Babel(app)  # Initialize Babel for handling translations

# Sample user data including names, locales, and timezones
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on the 'login_as' query parameter.
    Returns the user data if found, otherwise returns None.
    """
    login_id = request.args.get('login_as', '')  # Get the 'login_as' parameter from the query string
    if login_id:
        return users.get(int(login_id), None)  # Retrieve the user data by ID, or None if not found
    return None  # No user found


@app.before_request
def before_request() -> None:
    """Executes routines before handling each request.
    Sets the global user variable to be used in the request context.
    """
    user = get_user()  # Get the user based on the 'login_as' parameter
    g.user = user  # Store the user information in the global object


@babel.localeselector
def get_locale() -> str:
    """Selects the appropriate locale for rendering a web page.
    Checks for a specified locale, user locale, or header locale, falling back to the default locale.
    """
    locale = request.args.get('locale', '')  # Retrieve the 'locale' parameter from the query string
    if locale in app.config["LANGUAGES"]:  # Check if the provided locale is valid
        return locale  # Return the specified locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:  # Check if the user has a valid locale
        return g.user['locale']  # Return the user's locale if valid
    header_locale = request.headers.get('locale', '')  # Get the 'locale' from the request headers
    if header_locale in app.config["LANGUAGES"]:  # Validate the header locale
        return header_locale  # Return the header locale if valid
    return app.config['BABEL_DEFAULT_LOCALE']  # Fallback to the default locale defined in the config


@babel.timezoneselector
def get_timezone() -> str:
    """Selects the appropriate timezone for rendering a web page.
    Checks for a specified timezone, falling back to the user's timezone or the default timezone.
    """
    timezone = request.args.get('timezone', '').strip()  # Retrieve and clean the 'timezone' parameter from the query string
    if not timezone and g.user:  # If no timezone is specified, use the user's timezone if available
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone  # Return the valid timezone name
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']  # Fallback to the default timezone defined in the config


@app.route('/')
def get_index() -> str:
    """Renders the home/index page.
    """
    return render_template('7-index.html')  # Serve the HTML template for the index page


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the Flask application on all interfaces at port 5000
