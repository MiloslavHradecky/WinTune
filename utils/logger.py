import logging
import json
from logging.handlers import RotatingFileHandler
from utils.resources import resource_path


# --- Vlastní JSON formatter ---
class JsonFormatter(logging.Formatter):

    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "module": record.name,
            "message": record.getMessage()
        }
        return json.dumps(log_record, ensure_ascii=False)


# --- Inicializace logeru ---
def get_logger(name: str) -> logging.Logger:
    log_file_txt = resource_path("logs/app.log")
    log_file_json = resource_path("logs/structured.log")
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG)

    # TXT log s rotací
    txt_handler = RotatingFileHandler(log_file_txt, maxBytes=1_000_000, backupCount=5, encoding="utf-8")
    txt_formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    txt_handler.setFormatter(txt_formatter)
    logger.addHandler(txt_handler)

    # JSON log s rotací
    json_handler = RotatingFileHandler(log_file_json, maxBytes=1_000_000, backupCount=5, encoding="utf-8")
    json_handler.setFormatter(JsonFormatter())
    logger.addHandler(json_handler)

    return logger
