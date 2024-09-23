import os
from multiprocessing import cpu_count
from typing import Any

bind = f"0.0.0.0:{os.getenv('BIND_PORT', '5000')}"
workers = min(cpu_count() * 2 + 1, 3)
timeout = int(os.getenv("GUNICORN_TIMEOUT", "90"))


def child_exit(server: Any, worker: Any) -> None:  # pylint: disable=unused-argument
    """Called as soon as a worker ends. Pushes the PID of said worker to the
    Prometheus Metric Exporter.

    Args:
        server: the Arbiter that controls all Gunicorns in the master thread
        worker: Worker that has just exited.
    """
    pass