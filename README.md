#  BMW Telemetry App

A full-stack vehicle telemetry ingestion and real-time diagnostics web application. Designed to collect, store, and visualize live vehicle metrics—such as engine RPM, speed, coolant temperature, fuel consumption, and fault diagnostics—through an interactive dashboard.

---

##  Tech Stack

- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **Frontend & Visualization:** HTML/CSS, JavaScript, Chart.js
- **Containerization:** Docker & Docker Compose

---

##  Prerequisites

Ensure you have the following installed on your local machine:
- Docker & Docker Compose
- Python 3.10+ (if running locally outside of containers)
- Git

---

##  Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AndileKwaziMsomi/bmw-telemetry-app.git](https://github.com/AndileKwaziMsomi/bmw-telemetry-app.git)
   cd bmw-telemetry-app
   ```

2. **Configure environment variables:**
   Create a `.env` file in the root directory with your database and app credentials:
   ```env
   DB_HOST=db
   DB_PORT=5432
   DB_NAME=bmw_telemetry
   DB_USER=postgres
   DB_PASS=your_password
   ```

3. **Spin up with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

4. **Access the Dashboard:**
   Open your browser and navigate to `http://localhost:5000`.

---

##  Project Structure

```text
bmw-telemetry-app/
├── app/
│   ├── static/         # CSS, Chart.js scripts, and dashboard assets
│   ├── templates/      # HTML Jinja2 templates
│   ├── models.py       # PostgreSQL database models
│   ├── routes.py       # Flask API endpoints and dashboard views
│   └── telemetry.py    # Telemetry stream ingestion and processing
├── docker-compose.yml  # Multi-container orchestration
├── Dockerfile          # Python application image
├── requirements.txt    # Python dependencies
└── README.md
```

---

##  Key Features

- **Real-Time Telemetry Ingestion:** Captures and processes live vehicle sensor streams via REST API endpoints.
- **Historical Data Logging:** Persists trip logs, engine performance metrics, and diagnostic events in PostgreSQL.
- **Interactive Diagnostics Dashboard:** Visualizes speed, RPM, temperature trends, and system alerts in real time.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
