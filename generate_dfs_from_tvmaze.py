import numpy as np
import pandas as pd


from constant_information_generation import get_external


def generate_dataframes(
    objects, df_dates, df_generes, df_countries, df_weekDays, df_times
):

    columns_season = list(objects[0][0].get("show").keys()) + [
        "times",
        "country",
    ]

    df_episodes = pd.DataFrame(columns=objects[0][0].keys())
    df_seasons = pd.DataFrame(columns=columns_season)
    df_external = pd.DataFrame(
        columns=objects[0][0].get("show").get("externals").keys()
    )

    for day in objects:
        df_episodes = df_episodes.append(day, ignore_index=True)
        for show in day:

            idx_loc = len(df_seasons.index)
            image = None
            url_show = None
            raiting = None
            time = None

            df_seasons = df_seasons.append(show.get("show"), ignore_index=True)

            if show.get("show").get("_links"):
                url_show = (
                    show.get("show").get("_links").get("self").get("href")
                )
            if show.get("show").get("image"):
                image = show.get("show").get("image").get("medium")

            if show.get("show").get("rating"):
                raiting = show.get("show").get("rating").get("average")

            df_seasons["_links"] = url_show

            df_seasons["image"] = image
            df_seasons["rating"] = raiting

            country_key = "network"
            if not show.get("show").get(country_key):
                country_key = "webChannel"

            code_country = (
                show.get("show").get(country_key).get("country").get("code")
            )
            idx = np.nan
            if code_country:
                idx = df_countries.index[df_countries["code"] == code_country]
                idx = idx.values[0]

            df_seasons.loc[idx_loc, "country"] = idx

            generes = show.get("show").get("genres")
            row = df_generes.columns.isin(generes) * 1
            df_generes.loc[len(df_generes.index)] = list(row)

            days = show.get("show").get("schedule").get("days")
            row = df_weekDays.columns.isin(days) * 1
            df_weekDays.loc[len(df_weekDays.index)] = list(row)

            time = show.get("show").get("schedule").get("time")
            print(time)
            idx = np.nan
            if time:
                idx = df_times.index[df_times["times"] == time]
                print(idx)
                idx = idx.values[0]

            df_seasons.loc[idx_loc, "times"] = idx

            ended = show.get("show").get("ended")
            idx = np.nan
            if ended:
                idx = df_dates.index[df_dates["dates"] == ended]
                idx = idx.values[0]

            df_seasons.loc[idx_loc, "ended"] = idx

            df_external.append(get_external(show), ignore_index=True)

    df_episodes["airtime"] = df_episodes["airtime"].apply(
        lambda x: df_times.index[df_times["times"] == x]
    )
    df_episodes["airtime"] = df_episodes["airtime"].apply(lambda x: x.values[0])
    df_seasons.drop(labels="schedule", axis=1)

    return (df_episodes, df_seasons)


def convert_to_parquet(
    df_episodes,
    df_seasons,
    df_dates,
    df_generes,
    df_countries,
    df_weekDays,
    df_times,
):

    dict_df_to_convert = {
        "df_episodes": df_episodes,
        "df_seasons": df_seasons,
        "df_dates": df_dates,
        "df_generes": df_generes,
        "df_countries": df_countries,
        "df_weekDays": df_weekDays,
        "df_times": df_times,
    }

    for name_df, data_f in dict_df_to_convert.items():
        data_f.to_parquet(
            name_df,
            engine="pyarrow",
            compression="snappy",
        )


def official_site_list(df_seasons):

    lis_official_site = df_seasons["officialSite"].to_list()
    print("oficial Sites")
    print(lis_official_site)
