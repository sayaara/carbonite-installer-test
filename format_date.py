from dateutil import parser
from datetime import datetime

def format_date(input_date: str, output_format: str) -> str:
    # mapping the custom formats to python datetime strftime formats
    format_mapping = {
        "YYYY" : "%Y",  # 4 digit year e.g 2025
        "YY" : "%y",    # 2 digit year e.g. 25
        "MMMM" : "%B",    # full month name e.g. July
        "MMM" : "%b",   #short month name e.g. Jul
        "MM" : "%m",    # 2 digit numeric month e.g. 07
        "DD" : "%d",    # 2 digit numeric day e.g. 06
        "dddd" : "%A",  # full name of the day e.g. Sunday
        "ddd" : "%a",   # short name of the day  e.g. Sun
        "HH" : "%H",    # hour - 24 hr format
        "hh" : "%I",    # hour - 12 hr format
        "mm" : "%M",    # minute
        "ss" : "%s",    # seconds
        "AM/PM" : "%p"  # am/pm
    }

    # replace custom input format to python strftime format
    python_format = output_format
    for token in sorted(format_mapping, key=len, reverse=True):
        python_format = python_format.replace(token, format_mapping[token])
    
    try:
        python_date = parser.parse(input_date)
        return python_date.strftime(python_format)
    except Exception as e:
        return f"Error : could not parse date. details {e}"

if __name__ == "__main__":
    print(format_date("07-05-2025", "MM/DD/YYYY"))
    print(format_date("2025-07-06", "DD MMMM YY"))
    print(format_date("2025-Jul-061", "DD MMMM YY"))


