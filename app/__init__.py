"""
This is the flask app
"""
import datetime
from os import getenv
from dotenv import load_dotenv
from requests import get
from peewee import *
from flask import Flask, render_template, request
from playhouse.shortcuts import model_to_dict
from pylast import LastFMNetwork
import os



app = Flask(__name__)



@app.route("/")
def index():
    """
    Renders the homepage.
    """

    #repos = get("https://ghapi.dstn.to/aelxxs/pinned").json()["data"]

    return render_template("./home.html", title="Luis Marcano")

