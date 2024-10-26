import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


def get_env_variable(var_name: str, default_value=None):
    """Retrieve an environment variable or return a default value."""
    return os.getenv(var_name, default_value)


# Example usage of loading specific variables
API_TOKEN = get_env_variable("API_TOKEN", "YOUR_DEFAULT_API_TOKEN")
DATABASE_URL = get_env_variable("DATABASE_URL", "sqlite:///default.db")
