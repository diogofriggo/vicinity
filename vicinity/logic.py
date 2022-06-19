from pathlib import Path

import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go

from vicinity.app import app
from vicinity.core import read_cached_csv


EARTH_RADIUS_KM = 12742 / 2
LAT_COL = 'NumCoordNEmpreendimento'
LON_COL = 'NumCoordEEmpreendimento'


@app.callback([Output('table', 'data'), Output('table', 'columns')],
              Input('file_path', 'value'),
              Input('lat', 'value'),
              Input('lon', 'value'),
              Input('radius', 'value'))
def table_data_columns(file_path, lat, lon, radius):
    df = try_read_cached_csv(file_path)
    df[LAT_COL] = df[LAT_COL].str.replace(',', '.').astype(float)
    df[LON_COL] = df[LON_COL].str.replace(',', '.').astype(float)

    radius = parse_float(radius)
    if np.isnan(radius):
        radius = EARTH_RADIUS_KM

    lat = parse_float(lat)
    lon = parse_float(lon)
    if np.isnan(lat) or np.isnan(lon):
        return transform_df_into_dash_data_table(df)

    # TODO: calculate distances

def transform_df_into_dash_data_table(df):
    data = df.to_dict('records')
    columns = [{ 'name': c, 'id': c } for c in df]
    return data, columns


def try_read_cached_csv(file_path):
    try:
        return read_cached_csv(file_path)
    except:
        raise PreventUpdate


def parse_float(lat_or_lon):
    try:
        return float(lat_or_lon)
    except:
        return np.nan