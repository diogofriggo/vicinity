from dash import dash_table
import dash_bootstrap_components as dbc


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Label('SIGA .csv address', html_for='file_path'),
            dbc.Input(id='file_path', persistence=True),
        ], width=12),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label('Latitude (degrees)', html_for='lat_degrees'),
            dbc.Input(id='lat_degrees', persistence=True),
        ], width=2),
        dbc.Col([
            dbc.Label('Longitude (degrees)', html_for='lon_degrees'),
            dbc.Input(id='lon_degrees', persistence=True),
        ], width=2),
        dbc.Col([
            dbc.Label('Radius (km)', html_for='radius_km'),
            dbc.Input(id='radius_km', persistence=True),
        ], width=2),
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(id='table')
        ], width=12),
    ], style={'margin-top': '10px'}),
], fluid=True)