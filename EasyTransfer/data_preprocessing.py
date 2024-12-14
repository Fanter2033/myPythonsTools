import datetime
import re

def parse_input(arg):
    if arg in ["today", "t"]:
        return str(datetime.date.today())

    date_format_found = ""
    date_fill_sequence = ""

    patterns = {
        "YYYY": r"^\d{4}$",
        "YYYY-MM": r"^\d{4}-\d{2}$",
        "YYYY-MM-DD": r"^\d{4}-\d{2}-\d{2}$"
    }
    for format_name, pattern in patterns.items():
        if re.match(pattern, arg):
            date_format_found = format_name
    if date_format_found == "YYYY":
        date_fill_sequence = "-01-01"
    elif date_format_found == "YYYY-MM":
        date_fill_sequence = "-01"
    elif date_format_found == "":
        raise ValueError("Invalid date format. Expected formats: YYYY, YYYY-MM, YYYY-MM-DD")
    
    validate(arg + date_fill_sequence)
    return arg + date_fill_sequence
    
def validate(date_text):
    try:
        datetime.date.fromisoformat(date_text)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def parse_options(args):
    mode = list("0000")
    if args.recursive:
        mode[3] = "1"
    
    return mode
