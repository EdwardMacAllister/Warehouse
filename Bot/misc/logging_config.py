# logging_config.py

import logging
import os


def setup_logging():
    """Set up logging configuration."""
    log_file_path = os.path.join("logs", "bot.log")

    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Create a logger
    logger = logging.getLogger("BotLogger")
    logger.setLevel(logging.DEBUG)

    # Create file handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Set formatter for handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("Logging is set up and started.")

    return logger  # Return the logger instance


def log_info(message: str):
    logger = logging.getLogger("BotLogger")
    logger.info(message)


def log_error(message: str):
    logger = logging.getLogger("BotLogger")
    logger.error(message)
