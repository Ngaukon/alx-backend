#!/usr/bin/env python3
"""A basic Flask application.
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False  # Allow trailing slashes in routes


@app.route('/')
def get_index() -> str:
    """Render the home/index page.
    """
    return render_template('0-index.html')  # Serve the index HTML template


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the Flask app on host 0.0.0.0 and port 5000
