from flask import Flask

app = Flask(__name__)


@app.route('/api')
def api_version():
    return {'version': '1.0.0'}