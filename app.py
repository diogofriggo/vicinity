from dash import Dash
import dash_bootstrap_components as dbc
import gunicorn # whilst your local machine's webserver doesn't need this, Heroku's linux webserver (i.e. dyno) does. I.e. This is your HTTP server
from whitenoise import WhiteNoise # for serving static files on Heroku

from vicinity.app import app, server
from vicinity.logic import *

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
