import datetime
import re

def parse_input(arg):
    if arg == "today" or arg == "t":
        return str(datetime.date.today())

    format_found = ""
    fill_seq = ""

    patterns = {
        "YYYY": r"^\d{4}$",
        "YYYY-MM": r"^\d{4}-\d{2}$",
        "YYYY-MM-DD": r"^\d{4}-\d{2}-\d{2}$"
    }
    for format_name, pattern in patterns.items():
        if re.match(pattern, arg):
            format_found = format_name
    if format_found == "YYYY":
        fill_seq = "-01-01"
    elif format_found == "YYYY-MM":
        fill_seq = "-01"
    elif format_found == "":
        return ""
    
    validate(arg + fill_seq)
    return arg + fill_seq
    
def validate(date_text):
    try:
        datetime.date.fromisoformat(date_text)
    except ValueError:
        exit("Incorrect data format, should be YYYY-MM-DD")

def parse_options(args):
    mode = list("0000")
    if args.recursive:
        mode[3] = "1"
    
    return mode
