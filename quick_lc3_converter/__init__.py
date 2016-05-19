"""Initialize the quick_lc3_convert app"""
# pylint: disable=invalid-name,wrong-import-position
from os import getenv
from flask import Flask, render_template, request, url_for, Markup

app = Flask(__name__)

import hexAndLC3, binaryAndLC3
