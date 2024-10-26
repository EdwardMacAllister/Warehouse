# utils/validation_utils.py
import re


def is_valid_username(username):
    """
    Validates the username to ensure it meets certain criteria.

    :param username: Username string to validate
    :return: True if valid, otherwise False
    """
    if re.match("^[a-zA-Z0-9_]{3,}$", username):
        return True
    return False


def is_valid_password(password):
    """
    Validates the password strength.

    :param password: Password string to validate
    :return: True if valid, otherwise False
    """
    if len(password) >= 8:
        return True
    return False
