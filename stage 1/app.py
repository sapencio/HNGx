from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/get_info', methods=['GET'])
def get_info():
    try:
        slack_name = request.args.get('slack_name').title()
        track = request.args.get('track').title()
        current_day = datetime.datetime.now().strftime('%A')
        utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        response = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": "https://github.com/sapencio/HNGx/blob/master/stage%201/app.py",
            "github_repo_url": "https://github.com/sapencio/HNGx/tree/master",
            "status_code": 200
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({
            "error": str(e)
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)