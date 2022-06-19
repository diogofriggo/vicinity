from dash import Dash
import dash_bootstrap_components as dbc
import gunicorn # whilst your local machine's webserver doesn't need this, Heroku's linux webserver (i.e. dyno) does. I.e. This is your HTTP server
from whitenoise import WhiteNoise # for serving static files on Heroku

from vicinity.ui import layout

# AVAILABLE THEMES:
# CERULEAN , COSMO , CYBORG , DARKLY , FLATLY , JOURNAL , LITERA , LUMEN ,
# LUX , MATERIA , MINTY , PULSE , SANDSTONE , SIMPLEX , SKETCHY , SLATE ,
# SOLAR , SPACELAB , SUPERHERO , UNITED , YETI

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = layout
app.title = 'Vicinity'

server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)
