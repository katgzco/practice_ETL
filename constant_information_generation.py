from pycountry import countries, languages
import inspect
import sys
import numpy as np


def get_countries_info(objects):
    countries_info = {"code": "", "name": "", "timezone": ""}
    code = []
    name = []
    timezone = []

    for lis_dict_ in objects:
        for dict_ in lis_dict_:
            country_key = "network"
            if not dict_.get("show").get(country_key):
                country_key = "webChannel"
            info_country = dict_.get("show").get(country_key).get("country")
            if info_country:
                code.append(info_country.get("code"))
                name.append(info_country.get("name"))
                timezone.append(info_country.get("timezone"))

    countries_info = {
        "code": tuple(set(code)),
        "name": tuple(set(name)),
        "timezone": tuple(set(timezone)),
    }

    return countries_info


def get_external(dict_):
    externals = {"id": "", "imdb": "", "thetvdb": "", "tvrage": ""}
    externals_dict = dict_.get("show").get("externals")
    externals.update(
        {
            "id": dict_.get("id"),
            "imdb": externals_dict.get("imdb"),
            "thetvdb": externals_dict.get("thetvdb"),
            "tvrage": externals_dict.get("tvrage"),
        }
    )
    return externals


def get_genres(objects):
    genres = []
    for lis_dict_ in objects:
        for dict_ in lis_dict_:
            genres.append(dict_.get("show").get("genres"))
    genres = [item for elem in genres for item in elem]
    genres = set(genres)
    return genres


def get_min_date(objects):
    dates = []
    for lis_dict in objects:
        for dict_ in lis_dict:
            dates.append(dict_.get("airdate"))
            dates.append(dict_.get("show").get("ended"))
            dates.append(dict_.get("show").get("premiered"))

    min_date = min(i for i in dates if i is not None)
    max_date = max(i for i in dates if i is not None)

    return min_date, max_date
