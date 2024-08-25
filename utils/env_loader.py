from dotenv import load_dotenv


"""
Utility for loading environment variables.

This module provides a function to load environment variables from the .env file
using the python-dotenv library.

Modules:
    dotenv: Used to load environment variables from the .env file.

Functions:
    load_env_vars: Loads environment variables from the .env file.
"""


def load_env_vars():
    """
    Loads environment variables from the .env file into the environment.
    """
    load_dotenv()

