from dash import dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Label('File path', html_for='file_path'),
            dbc.Input(
                id='file_path',
                persistence=True),
        ], width=12),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label('Columns to plot', html_for='columns'),
            dcc.Dropdown(id='columns', multi=True),
        ], width=12),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label('X column (blank will default to df.index)', html_for='x_col'),
            dcc.Dropdown(id='x_col', persistence=True),
        ], width=4),
        dbc.Col([
            dbc.Label('Row start', html_for='row_start'),
            dbc.Input(id='row_start', persistence=True),
        ], width=1),
        dbc.Col([
            dbc.Label('Row end', html_for='row_end'),
            dbc.Input(id='row_end', persistence=True),
        ], width=1),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='output', style={'margin-top': '3px'})
        ], width=12),
    ]),
], fluid=True)