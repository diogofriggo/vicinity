from dash import Dash
import dash_bootstrap_components as dbc
from whitenoise import WhiteNoise # for serving static files on Heroku

# AVAILABLE THEMES:
# CERULEAN , COSMO , CYBORG , DARKLY , FLATLY , JOURNAL , LITERA , LUMEN ,
# LUX , MATERIA , MINTY , PULSE , SANDSTONE , SIMPLEX , SKETCHY , SLATE ,
# SOLAR , SPACELAB , SUPERHERO , UNITED , YETI

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Vicinity'

server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')