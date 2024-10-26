from Bot.error_handlers.logger import log_error


def handle_user_error(exception: Exception, user_message: str):
    """Handle a user-related error globally and provide user feedback."""
    log_error(str(exception))  # Log the exception details
    return user_message  # Return the user-friendly message
