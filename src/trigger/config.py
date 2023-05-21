import logging
import sys

class MessageIsNormal(logging.Filter):
    def filter(self, record):
        return record.levelname in ["DEBUG", "INFO", "WARNING"]
    
class MessageIsError(logging.Filter):
    def filter(self, record):
        return record.levelname in ["ERROR", "CRITICAL"]
    
bind = "0.0.0.0:8080"
logconfig_dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "info": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": sys.stdout,
            "filters": ["message_is_normal"]
        },
        "error": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": sys.stderr,
            "filters": ["message_is_error"]
        }
    },
    "filters": {
        "message_is_normal": {
            "()": MessageIsNormal
        },
        "message_is_error": {
            "()": MessageIsError
        }
    },
    "loggers": {
        "uvicorn.access": {
            "handlers": ["info"],
            "level": "INFO",
            "propagate": False
        },
        "uvicorn.error": {
            "handlers": ["error"],
            "level": "ERROR",
            "propagate": False
        }
    }
}