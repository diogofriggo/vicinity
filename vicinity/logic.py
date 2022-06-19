from pathlib import Path

import pandas as pd
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go

from vicinity.app import app
from vicinity.core import read_cached_csv

print('LOGIC.PY IS BEING IMPORTEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')

@app.callback(Output('x_col', 'options'),
              Input('file_path', 'value'))
def x_col_options(file_path):
    return get_options(file_path)


@app.callback(Output('columns', 'options'),
              Input('file_path', 'value'))
def columns_options(file_path):
    return get_options(file_path)


def get_options(file_path):
    print(f'get_options({file_path})')
    try:
        df = try_read_cached_csv(file_path)
        options = [{'label': c, 'value': c} for c in df]
        return options
    except:
        return []


@app.callback(Output('output', 'figure'),
              Input('file_path', 'value'),
              Input('columns', 'value'),
              Input('x_col', 'value'),
              Input('row_start', 'value'),
              Input('row_end', 'value'))
def output_figure(file_path, columns, x_col, row_start, row_end):
    if row_start is None:
        row_start = 0

    df = try_read_cached_csv(file_path)

    if row_end is None:
        row_end = len(df)

    x = df.index
    if x_col is not None:
        x = df[x_col]

    if columns is None or columns == []:
        columns = df.columns

    figure = go.Figure()
    sub_df = df.iloc[int(row_start):int(row_end)]
    for col in columns:
        y = sub_df[col]
        trace = go.Scatter(x=x, y=y, name=col)
        figure.add_trace(trace)

    return figure


def try_read_cached_csv(file_path):
    try:
        return read_cached_csv(file_path)
    except:
        raise PreventUpdate