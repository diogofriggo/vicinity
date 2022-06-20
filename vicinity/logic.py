from pathlib import Path

import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go

from vicinity.app import app
from vicinity import core


@app.callback([Output('table', 'data'), Output('table', 'columns')],
              Input('file_path', 'value'),
              Input('lat_degrees', 'value'),
              Input('lon_degrees', 'value'),
              Input('radius_km', 'value'))
def table_data_columns(file_path, lat_degrees, lon_degrees, radius_km):
    df = try_read_cached_csv(file_path)

    radius_km = parse_float(radius_km)
    if np.isnan(radius_km):
        radius_km = core.EARTH_DIAMETER_KM / 2.0

    lat_degrees = parse_float(lat_degrees)
    lon_degrees = parse_float(lon_degrees)
    if np.isnan(lat_degrees) or np.isnan(lon_degrees):
        return transform_df_into_dash_data_table(df)

    df = core.compute_vicinity(df, lat_degrees, lon_degrees, radius_km)
    return transform_df_into_dash_data_table(df)


def transform_df_into_dash_data_table(df):
    data = df.to_dict('records')
    columns = [{ 'name': c, 'id': c } for c in df]
    return data, columns


def try_read_cached_csv(file_path):
    test_df = core.read_cached_csv('data/siga-empreendimentos-geracao.csv')
    print(test_df)
    try:
        return core.read_cached_csv(file_path)
    except:
        raise PreventUpdate


def parse_float(value):
    try:
        return float(value)
    except:
        return np.nan