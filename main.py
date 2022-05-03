import numpy as np
import pandas as pd

from date_time_generation import generate_hours, generate_week_days
from constant_information_generation import (
    get_countries_info,
    get_external,
    get_genres,
    get_min_date,
)
from constant_dataframe_creation import (
    generate_df_dates,
    generate_df_times,
    generate_df_week_days,
    generate_df_generes,
    generate_df_countries,
    generate_df,
)
from extraction import create_json_objects, remove_iso_date, save_json
from generate_dfs_from_tvmaze import (
    generate_dataframes,
    convert_to_parquet,
    official_site_list,
)
from awss import upload_file, create_client


def main():
    # 1 - Generar Dataframes No dependientes
    times = generate_hours()
    weekDays = generate_week_days()
    df_times = generate_df_times(times)
    df_weekDays = generate_df_week_days(weekDays)
    # print(df_times)
    # print(df_weekDays)
    print("SE GENERARON DATAFRAMES")

    # 2 - Generar objeto
    objects = create_json_objects()
    print("SE CREO OBJETO")

    # # 3 Guardar en Gzip
    client = create_client("s3")
    save_json(objects, client)

    # 4 - Remover iso date
    objects = remove_iso_date(objects)
    print("SE REMOVIO FECHA")

    # 5 - Generar DATOS Dependientes
    min_date, max_date = get_min_date(objects)
    countries_info = get_countries_info(objects)
    genres = get_genres(objects)
    # print(min_date, max_date)
    # print(countries_info)
    # print(genres)
    print("SE GENERARON DATOS DEPENDIENTES")

    # # 6 - Crear datframes dependientes
    df_dates = generate_df_dates(min_date, max_date)
    df_generes = generate_df_generes(genres)
    df_countries = generate_df_countries(countries_info)
    # print(df_dates)
    # print(df_generes)
    # print(df_countries)
    print("SE GENERARON DATAFRAMES DEPENDIENTES")

    # 7 - Crear dataframes principales
    print("SE GENERO DATAFRAME PRINCIPAL")
    df_episodes, df_seasons = generate_dataframes(
        objects, df_dates, df_generes, df_countries, df_weekDays, df_times
    )

    official_site_list(df_seasons)

    convert_to_parquet(
        df_episodes,
        df_seasons,
        df_dates,
        df_generes,
        df_countries,
        df_weekDays,
        df_times,
    )


main()
