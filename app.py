from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def serve_survey():
    return send_from_directory('/app/templates', 'survey.html')

@app.route('/gmu_logo.png.jpg')
def serve_logo():
    return send_from_directory('/app', 'gmu_logo.png.jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)