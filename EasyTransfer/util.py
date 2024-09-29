import datetime
import platform

# CONSTANT
__author__ = "Fanter"
__version__ = "0.1.1"

SUPPORTED_CAMERAS_BRAND = ["Sony"]
WINDOWS_PACKAGES = []

START = 0
END  = 1

REC = 3
ALL = 2

# FUNCTIONS
def hi():
    print("Running on: " + platform.system() + " - version: "+ __version__ +"\nStart copying...")
    return platform.system()

def str_to_ts(strt):
    return datetime.datetime.strptime(strt, "%Y-%m-%d").timestamp()

def ts_to_str(ts):
    return str(datetime.datetime.fromtimestamp(ts).date())

def is_in_timeline(s, e, file):
    return int(file.stat().st_mtime) >= str_to_ts(s) and int(file.stat().st_mtime) <= str_to_ts(e)