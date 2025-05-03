import datetime
import re
from .util import AUTO, REC

def convertDate(duration_str) -> str:
    """
    Converts a duration string into a date string.
    """
    duration_str = duration_str.lower().strip()
    today = datetime.date.today()
    if duration_str in ["today", "t"]:
        return str(today)
    match = re.match(r"(\d+|[a-z]+)\s*(day|week|month|year)s?", duration_str)
    if not match:
        return duration_str
    
    value, unit = match.groups()
    if value.isdigit():
        numeric_value = int(value)
    else:
        raise ValueError("Invalid numeric value in duration.")
    today = datetime.date.today()
    unit_map = {
        "day": "days",
        "week": "weeks",
        "month": "months",
        "year": "years"
    }

    if unit in unit_map:
        if unit_map[unit] in ["days", "weeks"]:
            delta = datetime.timedelta(**{unit_map[unit]: numeric_value})
            result_date = today - delta
        elif unit == "month":
            year, month = divmod(today.month - numeric_value - 1, 12)
            result_date = today.replace(year=today.year + year, month=month + 1, day=1)
        elif unit == "year":
            result_date = today.replace(year=today.year - numeric_value)
    else:
        raise ValueError("Unsupported time unit.")
    return result_date.isoformat()

def parse_input(arg) -> str:
    """
    Parses the input date string and returns a standardized date format.
    Args:
        arg (str): The input date string. It can be one of the following:
            - "today" or "t": Returns the current date in "YYYY-MM-DD" format.
            - "YYYY": Converted to "YYYY-01-01".
            - "YYYY-MM": Converted to "YYYY-MM-01".
            - "YYYY-MM-DD": omplete date in "YYYY-MM-DD" format.
    Returns:
        str: The standardized date string in "YYYY-MM-DD" format if the input matches one of the patterns.
             Returns an empty string if the input does not match any pattern.
    """
    arg = convertDate(arg)

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
    
def validate(date_text) -> None:
    try:
        datetime.date.fromisoformat(date_text)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def parse_options(args) -> list:
    mode = list("0000")
    if args.recursive:
        mode[REC] = "1"
    if args.auto:
        mode[AUTO] = "1"
    return mode
