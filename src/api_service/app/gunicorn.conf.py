import os

bind = f"0.0.0.0:{os.getenv('BIND_PORT', '5000')}"
workers = 1
timeout = int(os.getenv("GUNICORN_TIMEOUT", "90"))
