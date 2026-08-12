import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/v1/telemetry', methods=['GET'])
def get_telemetry():
    return jsonify({
        "vehicle_id": "BMW-IX-0402",
        "speed": random.randint(80, 160),
        "battery_level": random.randint(40, 98),
        "status": "OK"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)