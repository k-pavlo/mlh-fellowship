import os
from flask import Flask, abort, render_template, request
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv
from peewee import *
import datetime
import json

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

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

@app.route('/app/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    
    return model_to_dict(timeline_post)

@app.route('/app/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in 
TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/app/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    try:
        last_post = TimelinePost.select().order_by(TimelinePost.created_at.desc()).get()
        last_post.delete_instance()
    except:
        return "There are no posts in the timeline."
    return "The last post have been deleted."