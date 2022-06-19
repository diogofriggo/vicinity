from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Label('SIGA .csv address', html_for='file_path'),
            dbc.Input(
                id='file_path',
                persistence=True),
        ], width=12),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label('Latitude', html_for='lat'),
            dbc.Input(id='lat'),
        ], width=2),
        dbc.Col([
            dbc.Label('Longitude', html_for='lon'),
            dbc.Input(id='lon'),
        ], width=2),
        dbc.Col([
            dbc.Label('Radius (km)', html_for='radius'),
            dbc.Input(id='radius'),
        ], width=2),
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(id='table')
        ], width=12),
    ], style={'margin-top': '10px'}),
], fluid=True)