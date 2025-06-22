import os
from flask import Flask, abort, render_template, request
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
        with open(os.path.join(app.root_path, 'data', 'profile_summary.json'), 'r') as file:
            data = json.load(file)
        return render_template('profile_summary.html', title="Profile Summary", profile_summary=data, url=os.getenv("URL"))
    except FileNotFoundError:
        abort(404, description="Profile summary data not found.")
    
@app.route('/map')
def map():
    try:
        API_KEY = os.getenv("API_KEY")
        with open(os.path.join(app.root_path, 'data', 'map.json'), 'r') as file:
            places = json.load(file)
        return render_template('map.html', title="My Travel Map", places=places, API_KEY=API_KEY, url=os.getenv("URL"))
    except FileNotFoundError:
        abort(404, description="Map data not found.")

@app.route('/hobbies')
def hobbies():
    try:
        with open(os.path.join(app.root_path, 'data', 'hobbies.json'), 'r') as file:
            data = json.load(file)
        return render_template('hobbies.html', title="Hobbies", hobbies=data, url=os.getenv("URL"))
    except FileNotFoundError:
        abort(404, description="Hobbies data not found.")