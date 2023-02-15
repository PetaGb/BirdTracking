from pathlib import Path

from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import gmap
from bokeh.models import GMapOptions, ZoomInTool, ZoomOutTool, Range1d
from dotenv import load_dotenv
import os

app = Flask(__name__)

dotenv_path = Path('/.env')
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("API_KEY")

bokeh_width, bokeh_height = 1250, 640
lat, lon = 41.2437, 6.0251

def plot(lat, lng, zoom=(5), map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng, map_type=map_type, zoom=zoom)
    p = gmap(api_key, gmap_options, title='2016 Autumn move of Mirabell', width=bokeh_width, height=bokeh_height)
    p.x_range = Range1d(start=-180, end=180)
    p.y_range = Range1d(start=-90, end=90)
    p.add_tools(ZoomInTool(), ZoomOutTool())
    p.circle([8.907325], [47.7351469], size=10, alpha=0.5, color='red')
    return p

@app.route("/")

def index():
    p = plot(lat, lon)
    script, div = components(p)

    return render_template("index.html", script=script, div=div)

if __name__ == "__main__":
    app.run(debug=True)
