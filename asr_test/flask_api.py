from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/time')
def get_time():
    now = datetime.now()
    return jsonify({'time': now.strftime('%Y-%m-%d %H:%M:%S')})


@app.route('/fleurs')
def get_fleurs_dataset():
    return


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
