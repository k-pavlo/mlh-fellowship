import os
from flask import Flask, abort, render_template, request
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)

def load_json_file(filename):
    path = os.path.join(app.root_path, 'data', filename)
    with open(path, 'r') as file:
        return json.load(file)

# Make footer_data accesable globally
@app.context_processor
def inject_footer_data():
    try:
        footer_data = load_json_file('footer.json')
        return dict(footer_data=footer_data)
    except FileNotFoundError:
            abort(404, description="Footer data not found.")

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/profile_summary')
def profile_summary():
    try:
        data = load_json_file('profile_summary.json')
        return render_template('profile_summary.html', title="Profile Summary", profile_summary=data, url=os.getenv("URL"))
    except FileNotFoundError:
        abort(404, description="Profile summary data not found.")
    
@app.route('/map')
def map():
    try:
        API_KEY = os.getenv("API_KEY")
        places = load_json_file('map.json')
        return render_template('map.html', title="My Travel Map", places=places, API_KEY=API_KEY, url=os.getenv("URL"))
    except FileNotFoundError:
        abort(404, description="Map data not found.")

@app.route('/hobbies')
def hobbies():
    try:
        data = load_json_file('hobbies.json')
        return render_template('hobbies.html', title="Hobbies", hobbies=data, url=os.getenv("URL"))
    except FileNotFoundError:
        abort(404, description="Hobbies data not found.")