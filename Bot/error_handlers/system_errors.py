from Bot.error_handlers.logger import log_error


def handle_system_error(exception: Exception):
    """Handle a system-related error globally."""
    log_error(str(exception))  # Log the exception details
    return "Произошла ошибка на стороне системы. Пожалуйста, попробуйте позже."  # Generic error message
