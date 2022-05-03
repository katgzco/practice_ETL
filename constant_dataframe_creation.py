import datetime
import pandas as pd


def generate_df_dates(start_date, end_date):
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    date_generated = pd.date_range(start, end)
    date_generated.strftime("%Y-%m-%d")
    df = pd.DataFrame()
    df["dates"] = date_generated
    return df


def generate_df_times(times):
    df_hours = generate_df(times)
    df_hours.rename(columns={0: "times"}, inplace=True)
    return df_hours


def generate_df_week_days(weekDays):
    df_weekDays = generate_df_columns(weekDays)
    return df_weekDays


def generate_df_generes(generes):
    df_generes = generate_df_columns(generes)
    return df_generes


def generate_df_countries(countries):
    df_countries = generate_df(countries)
    return df_countries


def generate_df_columns(columns_df):
    df = pd.DataFrame(columns=columns_df)
    return df


def generate_df(data):
    df = pd.DataFrame(data)
    return df
