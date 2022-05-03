import requests
from calendar import monthrange
from multiprocessing import Pool
import os
import pandas as pd

from save_json_to_gz import save_json_gz


def create_days_range(year, month):
    """creates the date ranges to perform the query in the api

    Args:
        year (int): year to generate rank
        month (int): month to generate rank

    Returns:
        list: range of days generated
    """
    num_days = monthrange(year, month)[1]
    days = [f"{day:02}" for day in range(1, (num_days + 1))]
    return days


def get_jsons(day):
    """makes the request to the api and obtains the rank

    Args:
        day (str): _description_

    Returns:
        dict: json with the information of the consulted day
    """
    url = "https://api.tvmaze.com/schedule"
    date_iso = f"2020-12-{day}"
    payload = {"date": date_iso}
    return (date_iso, (requests.get(url, params=payload)).json())


def create_json_objects():
    """calls the function that makes the request to the api and to
    the function that generates the range for the query

    Returns:
        tuple: tuple of lists with generated jsons and date range
    """
    with Pool((os.cpu_count() - 2)) as p:
        objects = p.map(get_jsons, create_days_range(2020, 12))

    return objects


def save_json(json_objects):
    with Pool((os.cpu_count() - 2)) as p:
        p.starmap(save_json_gz, json_objects)


def remove_iso_date(objects):
    objects = tuple(map(lambda x: x[1], objects))
    return objects
