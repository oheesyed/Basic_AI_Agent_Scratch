import os
import yaml  
from dotenv import load_dotenv


def load_config(file_path):
    """
    Load configuration from a YAML file and set environment variables.

    This function reads a YAML file specified by file_path, loads its contents,
    and sets each key-value pair as an environment variable.

    Args:
        file_path (str): The path to the YAML configuration file.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
        yaml.YAMLError: If there's an error parsing the YAML file.
    """
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
        for key, value in config.items():
            os.environ[key] = str(value)  # Convert value to string for consistency



            