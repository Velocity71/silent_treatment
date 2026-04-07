# src/silent_treatment/core/ui/cli.py
# user command-line interface

# logging configuration {{{

from silent_treatment import LOGLEVEL
import logging

logging.basicConfig(
    level=LOGLEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s",
    )

logger = logging.getLogger(__name__)

# }}}

from silent_treatment.core import read, write, edit, delete

def main():
    logger.INFO("beginning command-line interface")
    master_password = input("Enter master password: ")
    logger.INFO("User has input master password {master_password}")

    loop:
        match input("Read, write, or delete a password?[r/w/d]: "):
            case "r":
                print(read(input("Enter key: "))
            case "w":
                match input("New password or edit a current one?[n/e]: "):
                    case "n":
                        new(input("Enter key: "), input("Enter value: "))
                    case "e":
                        raise NotImplementedError
                    case _:
                        raise ValueError
            case "d":
                delete(input("Enter key: "))
            case _:
                raise ValueError

        match input("Restart or exit?[r/e]: "):
            case "r":
                continue
            case "e":
                exit()
            case _:
                raise ValueError

