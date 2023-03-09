from pathlib import Path
from flask import Flask, render_template
from bokeh.embed import components
from dotenv import load_dotenv
import os

import bokeh_plot


app = Flask(__name__)

dotenv_path = Path('/.env')
load_dotenv(dotenv_path=dotenv_path)
api_key = os.getenv("API_KEY")
lat, lon = 41.2437, 6.0251


@app.route("/")
def index():
    p = bokeh_plot.plot(lat, lon)
    script, div = components(p)
    return render_template("index.html", script=script, div=div)


if __name__ == "__main__":
    app.run(debug=True)
