from flask import Flask
import sqlite3


app = Flask(__name__)

connection = sqlite3.connect('')