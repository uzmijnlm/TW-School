#!/usr/bin/env python3

from . import app
from .models import User
from . import db


@app.route('/')
def index():
    return 'index page'


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')
