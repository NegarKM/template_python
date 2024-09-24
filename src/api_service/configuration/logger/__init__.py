import os
import json
import logging
from logging import LogRecord
from datetime import datetime


class Logger:
    def __init__(self, level: int = logging.INFO):
        self.configured_logger: logging.Logger = logging.getLogger("sample-api")

        self.configured_logger.propagate = False
        self.configured_logger.setLevel(level)

        self.configured_logger.addHandler(Logger.configure_handler())

    @staticmethod
    def configure_handler() -> logging.Handler:
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        return handler

    def get_logger(self) -> logging.Logger:
        return self.configured_logger


class JsonFormatter(logging.Formatter):
    def format(self, record: LogRecord) -> str:
        exception = None

        if record.exc_info is not None:
            exception = logging.Formatter.formatException(self, record.exc_info)

        result = {
            "date": datetime.utcnow().isoformat(),
            "exception": exception.split(os.linesep) if exception else None,
            "level": record.levelname,
        }

        if isinstance(record.msg, dict):
            result = {**result, **record.msg}
        else:
            result["message"] = record.msg

        json_result = json.dumps(result, indent=2, sort_keys=True)
        return json_result
