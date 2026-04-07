# src/silent_treatment/__main__.py
# entry module for silent_treatment package

# logging configuration {{{

from silent_treatment import LOGLEVEL
import logging

logging.basicConfig{
    level=LOGLEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s",
    )

logger = logging.getLogger(__name__)

# }}}

from .main import main

if __name__ == "__main__":
    logger.INFO("Entry point called.")
    main()
