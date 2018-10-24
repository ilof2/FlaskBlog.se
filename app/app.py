from flask import Flask
from config import Configuration

import view


app = Flask(__name__)
app.config.from_object(Configuration)