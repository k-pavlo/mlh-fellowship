import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/profile_summary')
def profile_summary():
    try:
        with open('app/data/profile_summary.json', 'r') as file:
            data = json.load(file)
        return render_template('profile_summary.html', title="Profile Summary", profile_summary=data, url=os.getenv("URL"))
    except FileNotFoundError:
        return "Profile summary not found."