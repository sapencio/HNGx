from flask import Flask, make_response
from datetime import datetime, timezone

app = Flask(__name__)
resp = make_response(200, 'OK')

@app.route('/')
def hello(slack_name: str, track: str = None):
    return {
        "slack_name": slack_name,
        "current_date": datetime.now().strftime("%A"),
        "utc_date": datetime.now(timezone.utc),
        "track": track,
        "github_file_url": "https://github.com/sapencio/HNGx/blob/master/stage%201/app.py",
        "github_repo_url": "https://github.com/sapencio/HNGx/tree/master",
        "status_code": resp,
    }