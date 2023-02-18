from bokeh.models import GMapOptions, Range1d, ZoomInTool, ZoomOutTool, HoverTool
from bokeh.plotting import gmap
import pandas as pd

from main import api_key

bokeh_width, bokeh_height = 1250, 640

df = pd.read_csv("mirabell_2016.csv")
latitudes = df["location_latitude"].values
longitudes = df["location_longitude"].values



def plot(lat, lng, zoom=5, map_type='roadmap'):


    gmap_options = GMapOptions(lat=lat, lng=lng, map_type=map_type, zoom=zoom)
    p = gmap(api_key, gmap_options, title='2016 Autumn move of Mirabell',
             width=bokeh_width, height=bokeh_height)

    p.x_range = Range1d(start=-180, end=180)
    p.y_range = Range1d(start=-90, end=90)
    p.add_tools(ZoomInTool(), ZoomOutTool())

    red_circle = p.circle(longitudes[:180], latitudes[:180], size=7, alpha=0.5, color='red')
    blue_circle = p.circle(longitudes[180:], latitudes[180:], size=7, alpha=0.5, color='blue')


    p.add_tools(HoverTool(
        tooltips=[
            ("Link", "<a href='https://www.example.com' target='_blank'>Click Here</a>")
        ],
        renderers=[red_circle]
    ))

    return p
