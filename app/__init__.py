import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/profile_summary')
def profile_summary():
    profile_summary = {
        "name": "Firstname Lastname",
        "work_experiences": [
            {
                "position": "Job Title",
                "company": "Company Name",
                "start": "Jan 20XX",
                "end": "Dec 20XX",
                "description": "Brief description of responsibilities and achievements."
            },
            {
                "position": "Another Role",
                "company": "Another Company",
                "start": "Feb 20XX",
                "end": None,
                "description": "Optional second job experience, currently ongoing."
            }
        ],
        "education": [
            {
                "degree": "Degree Title",
                "institution": "University Name",
                "year": "20XX",
                "details": "Short summary of your academic focus or projects."
            },
            {
                "degree": "Another Degree",
                "institution": "Institution Name",
                "year": "20YY",
                "details": "Additional academic details or thesis title."
            }
        ],
        "hobbies": [
            "Example hobby one",
            "Example hobby two",
            "Another sample interest"
        ],
        "social_links": [
        {"platform": "GitHub", "url": "https://github.com/MLH"},
        {"platform": "LinkedIn", "url": "https://www.linkedin.com/company/major-league-hacking/posts/?feedView=all"}
        ]
    }

    return render_template('profile_summary.html', title="Profile Summary", profile_summary = profile_summary, url=os.getenv("URL"))