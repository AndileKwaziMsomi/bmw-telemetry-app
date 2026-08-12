FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files (including app.py and templates/)
COPY . .

EXPOSE 5001

CMD ["python", "app.py"]