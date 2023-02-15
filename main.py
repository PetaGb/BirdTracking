from pathlib import Path

from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from dotenv import load_dotenv
import os


app = Flask(__name__)


dotenv_path = Path('/home/peter/PycharmProjects/BirdTracking/.env')
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("API_KEY")
#"AIzaSyC00_XUTfguqC-QIuFD4cdOAe_EA6jSpsg"

bokeh_width, bokeh_height = 500, 400
lat, lon = 46.2437, 6.0251

def plot(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng, map_type=map_type, zoom=zoom)
    p = gmap(api_key, gmap_options, title='Pays de Gex', width=bokeh_width, height=bokeh_height)
    return p

@app.route("/")

def index():
    p = plot(lat, lon)
    script, div = components(p)

    return render_template("index.html", script=script, div=div)

if __name__ == "__main__":
    app.run(debug=True)
