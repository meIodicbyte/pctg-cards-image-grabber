import logging
import os

def logger_setup(name: str) -> logging.Logger:

    os.makedirs("logs", exist_ok=True)
    log_file = os.path.join("logs", f"{name}.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(log_file)
        
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger