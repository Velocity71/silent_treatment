# src/silent_treatment/core/file_manager.py
# datafile interface (e.g. reading and writing key-value pairs)

# note: datafile is formatted by "key:value\n" 
import errno
from silent_treatment import PATH, LOGLEVEL
import logging

logging.basicConfig(
    level=LOGLEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s",
    )

logger = logging.getLogger(__name__)

# simplified file opening utilities {{{

def checkfile(): # create file if it doesn't exist
    logger.debug("executing file check...")
    try:
        open(PATH, "x")
    except OSError as e:
        match e.errno:
            case errno.EEXIST: # throws if file exists, not a problem
                logger.debug("FileFound error thrown: file exists.")
                return
            case _:
                raise
    else:
        logger.debug("no errors thrown: file does not exist and was created.")
    finally:
        logger.debug("file check complete.")

def readfile():
    logger.debug("file opened to read.")
    return open(PATH, "r")

def appendfile():
    logger.debug("file opened to append.")
    return open(PATH, "a")

def writefile():
    logger.debug("file opened to write.")
    return open(PATH, "w")

# }}}

# file search utilities {{{

def getlines(): # return a list of all lines in the file
    logger.debug("a list of lines in the file was requested.")
    with readfile() as file:
        return file.readlines()

def getindex(key): # return the index of the line containing the key
    logger.debug(f"the index of the line containing {key=} was requested.")
    for index, line in enumerate(getlines()):
        if line.startswith(f"{key}:"):
            logger.debug(f"{key=} found on line {index=}, returning index.")
            return index

    # if key is not found return ValueError
    logger.critical(f"{key=} was not found in file, raising ValueError.")
    raise ValueError(f"{key=} not found in file")

def getline(key): # return the value of the line containing the key
    logger.debug(
        f"the value of the line containing {key=} was requested, \
        returning associated value {getlines()[getindex(key)]}"
        )
    return getlines()[getindex(key)]

# }}}

# core logic functions (read, write, edit, delete) {{{

def read(key): # return a value associated with a key
    logger.debug(
        f"the value associated with {key=} was requested, \
        returning associated value {getline(key).split(':', 1)[1]}" \
        )
    return getline(key).split(":", 1)[1]


def new(key, value): # append a key-value pair to the file
    logger.debug(f"writing new pair {key}:{value}.")
    with appendfile() as file:
        file.write(f"{key}:{value}\n")

# edit an existing key-value pair
def edit(key=None, newkey=None, newvalue=None):
    logger.debug(f"editing a pair using {key=},{newkey=},{newvalue=}...")
    raise NotImplementedError

def delete(key): # delete a key-value pair
    logger.debug(f"deleting pair {key=}:value={read(key)}...")

    lines = getlines() # obtain copy of file
    del lines[getindex(key)] # delete line containing pair

    with writefile() as file:
        file.writelines(lines) # write edited data to file

# }}}
