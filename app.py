from flask import Flask, jsonify
import datetime, platform

app = Flask(__name__)

@app.route('/api/v1/telemetry')
def get_telemetry():
    return jsonify({
        "vehicle_id": "BMW-i4-M50-2026",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "Optimal",
        "battery_pct": 84,
        "speed_kmh": 110,
        "os_platform": platform.platform()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)