import logging

# Configure logging
logging.basicConfig(
    filename='bot_errors.log',  # Specify your log file
    level=logging.ERROR,  # Set the logging level to ERROR
    format='%(asctime)s:%(levelname)s:%(message)s'
)


def log_error(error_message: str):
    """Log an error message to the specified log file."""
    logging.error(error_message)
