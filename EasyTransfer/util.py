import datetime
import platform
import json
import os
import time

# CONSTANT
__author__ = "Fanter"
__version__ = "0.1.2"

SUPPORTED_CAMERAS_BRAND = ["Sony"]
WINDOWS_PACKAGES = []

CONFIG_FILE = "./config.json"

START = 0
END  = 1

REC = 3
ALL = 2
AUTO = 1

# FUNCTIONS
def hi():
    print("Running on: " + platform.system() + " - version: "+ __version__ +"\nStart copying...")
    return platform.system()

def str_to_ts(strt) -> float:
    return datetime.datetime.strptime(strt, "%Y-%m-%d").timestamp()

def ts_to_str(ts) -> str:
    return str(datetime.datetime.fromtimestamp(ts).date())

def is_in_timeline(s, e, file) -> bool:
    creation_time = os.path.getmtime(file)
    return creation_time >= str_to_ts(s) and creation_time <= str_to_ts(e)

def load_config(confFile:str = CONFIG_FILE) -> dict:
    with open(confFile, 'r') as f:
        return json.load(f)
    return config