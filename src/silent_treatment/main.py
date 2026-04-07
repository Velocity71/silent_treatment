# src/silent_treatment/main.py
# main module of the silent_treatment package

from silent_treatment import __version__
from silent_treatment.core import *

def main():
    logger.debug("Main method called.")
    print(f"silent_treatment version: {__version__}")
    print("Running filechecks...")
    checkfile()
    print("File checks complete.")
    
    print(" -- NEW TEST --")
    new(input("key: "), input("value: "))
    
    print(" -- READ TEST --")
    print("value is: " + read(input("key: ")))

    print(" -- DELETE TEST --")
    delete(input("key: "))
    read(input("key: "))

if __name__ == "__main__":
    main()
