from dash import Dash
import dash_bootstrap_components as dbc

# AVAILABLE THEMES:
# CERULEAN , COSMO , CYBORG , DARKLY , FLATLY , JOURNAL , LITERA , LUMEN ,
# LUX , MATERIA , MINTY , PULSE , SANDSTONE , SIMPLEX , SKETCHY , SLATE ,
# SOLAR , SPACELAB , SUPERHERO , UNITED , YETI

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])