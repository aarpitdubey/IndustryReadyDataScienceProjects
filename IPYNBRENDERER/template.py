# import necessary libraries

import os 

from pathlib import Path # this library is use to make the application OS independent and,
# it appends path according to the OS

import logging # to track the logs or for debugging purpose

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

# for taking suggestion from user for the project name
while True: 
    project_name = input("Enter Project Name:  ")
    if project_name != '':
        break
    
logging.info(f"Creating project by name: {project_name}")

# list pf files:

list_of_files = [
    
    ".github/workflows/.gitkeep",
    # To keep all the action files which will help to check certain checks.
    # gitkeep is a dummy empty file, it doesn't do anything, in order to keep you project structure intact, on github
    # It is needed to kep empty file or directory in github otherwise, an empty directory or files will never be uploaded on to github.

    f"src/{project_name}/__init__.py",
    # src folder keeps all the scripts
    # __init__.py tells that it is a project.
    
    f"test/__init__.py",
    #testing files
    
    f"test/unit/__init__.py",
    # Unit testing
    
    f"test/integration/__init__.py",
    # Integration testing
    
    "init_setup.sh",
    # This will help to create a repository like to setup all the basic enviroment (conda environement)
    
    "requirements.txt",
    # It contains all the requirements and dependencies needed
    
    "requirements_dev.txt",
    # Only be used for testing purposes
    
    "setup.py",
    # to setup all the dependencies
    
    "pyproject.toml",
    
    "setup.cfg",
    
    "tox.ini"
    # to test python package in various environments
    
]

for filepath in list_of_files:
    filepath = Path(filepath) 
    filedir, filename = os.path.split(Path(filepath))
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for {filename}")
        
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already  present at: {filepath}")