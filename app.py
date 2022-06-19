from dash import Dash
import gunicorn # whilst your local machine's webserver doesn't need this, Heroku's linux webserver (i.e. dyno) does. I.e. This is your HTTP server

from vicinity.app import app, server
from vicinity.ui import layout
from vicinity.logic import *

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
