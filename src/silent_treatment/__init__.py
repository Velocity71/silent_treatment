# src/silent_treatment/__init__.py
# silent_treatment package

# read version from pyproject.toml
from importlib.metadata import version
__version__ = version("silent_treatment")

# expose PATH and LOG variables from config.py
from .config import PATH, LOGLEVEL
