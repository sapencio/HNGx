from flask import Flask
from datetime import datetime, timezone
import requests

app = Flask(__name__)
response = requests.get()

@app.route('/')
def hello(slack_name: str, track: str = None):
    return {
        "slack_name": slack_name,
        "current_date": datetime.now().strftime("%A"),
        "utc_date": datetime.now(timezone.utc),
        "track": track,
        "github_file_url": "https://github.com/sapencio/HNGx/blob/master/stage%201/script.py",
        "github_repo_url": "https://github.com/sapencio/HNGx/tree/master",
        "status_code": response(200, "OK"),
    }