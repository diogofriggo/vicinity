from dash import Dash
import gunicorn # whilst your local machine's webserver doesn't need this, Heroku's linux webserver (i.e. dyno) does. I.e. This is your HTTP server
from whitenoise import WhiteNoise # for serving static files on Heroku

from vicinity.ui import layout
from vicinity.logic import *
from vicinity.app import app

# All callbacks must be defined before the server starts

app.layout = layout
app.title = 'Vicinity'

server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
