import logging
from pathlib import Path

path_log = Path.cwd() / "app_errors.log"

logging.basicConfig(
    filename=path_log,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class AppError(Exception):
    def __init__(self, message, code=500):
        super().__init__(message)
        self.message = message
        self.code = code
        logging.error(f"AppError: {message}") 