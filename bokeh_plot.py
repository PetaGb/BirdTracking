from bokeh.models import GMapOptions, ZoomInTool, ZoomOutTool, TapTool, OpenURL, HoverTool
import pandas as pd
from bokeh.plotting import gmap
from main import api_key


bokeh_width, bokeh_height = 1250, 640
df = pd.read_csv("mirabell_2016.csv")
latitudes = df["location_latitude"].values
longitudes = df["location_longitude"].values
latitude = 47.7352829
longitude = 8.9074951
url = 'https://en.wikipedia.org/wiki/White_stork'


def plot(lat, lng, zoom=5, map_type='roadmap'):

    gmap_options = GMapOptions(lat=lat, lng=lng, map_type=map_type, zoom=zoom)
    p = gmap(api_key, gmap_options, title='2016 the move of Mirabell',
             width=bokeh_width, height=bokeh_height)

    p.legend.location = "top_left"
    p.legend.title = "Circles legend"
    p.legend.click_policy = "hide"

    p.add_tools(ZoomInTool(), ZoomOutTool(), TapTool())
    hover = HoverTool(tooltips=[("Name", "Mirabell"), ("URL", f'{url}')])
    p.add_tools(hover)
    taptool = p.select(type=TapTool)
    taptool.callback = OpenURL(url=url)

    circles(latitudes, longitudes, p)

    return p



def circles(latitudes, longitudes, p):

    red = p.circle(longitudes[:180], latitudes[:180], size=7, alpha=0.5, color='red', legend_label="spring move")
    blue = p.circle(longitudes[180:], latitudes[180:], size=7, alpha=0.5, color='blue', legend_label="autumn move")
    black = p.triangle(longitude, latitude, size=15, alpha=0.5, color='black', legend_label="interactive circles")

    return red, blue, black