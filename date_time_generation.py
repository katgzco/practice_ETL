import datetime
import pandas as pd
import datetime


def generate_hours():
    times = [
        f"{hour:02}:{minute:02}"
        for hour in range(0, 24)
        for minute in range(0, 60)
    ]
    return times


def generate_week_days():
    weekDays = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
    return weekDays
