# silent_treatment
## A password manager prototype written in Python.
<img src="silent_treatment.png"  width="200" height="200">

# Quick Documentation
## Dependencies
Currently the only dependency is that you have Python 3.10 or higher installed.
All dependencies are listed in `environment.yml` and `pyproject.toml`

### A note for Conda users
The provided `environment.yml` file can be used to create a Conda environment
with all required dependencies. As a refresher, execute:
```
conda env create -f environment.yml
```
and
```
conda activate silent_treatment
```

Fun fact: you can run a command inside a Conda environment without activating it
by running:
```
conda run -n my_environment my command
```

## How to run
The program is not currently available on any package managers so you will have
to build/run the program yourself. But don't fret this is very easy. After
downloading or cloning the repository you have a few options, all of which
assume you are in the root directory of the repository.

### Method 1: Direct execution (no installation required)
You may run the application without local installation. You can either directly
execute the main module script using:
```
python3 src/silent_treatment/main.py
```
or run the package by executing:
```
python3 -m silent_treatment
```
*from inside the source directory `src`*.

### Method 2: Installing the package locally
You may choose to install the package locally. To do this, execute:
```
pip3 install .
```
If you would like to edit live, add with the `-e` flag.

At this point you can choose to execute with the two above commands or you can
use either of the following commands:
```
run
```
(build script, identical to executing main module script)
```
python3 -m silent_treatment
```
(no need to change directory this time)
