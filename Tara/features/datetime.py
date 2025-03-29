import datetime

def get_date(format="%b %d %Y"):
    """Returns the current date in the specified format."""
    try:
        return datetime.datetime.now().strftime(format)
    except Exception as e:
        print(f"TARA: Error fetching date - {e}")
        return False

def get_time(format="%H:%M:%S"):
    """Returns the current time in the specified format."""
    try:
        return datetime.datetime.now().strftime(format)
    except Exception as e:
        print(f"TARA: Error fetching time - {e}")
        return False
