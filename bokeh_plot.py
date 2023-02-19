from bokeh.models import GMapOptions, Range1d, ZoomInTool, ZoomOutTool, TapTool, OpenURL, ColumnDataSource, \
    LabelSet
import pandas as pd
from bokeh.plotting import gmap


from main import api_key

bokeh_width, bokeh_height = 1250, 640

df = pd.read_csv("mirabell_2016.csv")
latitudes = df["location_latitude"].values
longitudes = df["location_longitude"].values
latitude = 47.7352829
longitude = 8.9074951
link_name = 'Click here'
url = 'https://en.wikipedia.org/wiki/White_stork'


def plot(lat, lng, zoom=5, map_type='roadmap'):

    gmap_options = GMapOptions(lat=lat, lng=lng, map_type=map_type, zoom=zoom)
    p = gmap(api_key, gmap_options, title='2016 Autumn move of Mirabell',
             width=bokeh_width, height=bokeh_height)

    p.x_range = Range1d(start=-180, end=180)
    p.y_range = Range1d(start=-90, end=90)
    p.add_tools(ZoomInTool(), ZoomOutTool(), TapTool())

    p.circle(longitudes[:180], latitudes[:180], size=7, alpha=0.5, color='red')
    p.circle(longitudes[180:], latitudes[180:], size=7, alpha=0.5, color='blue')
    p.circle(longitude, latitude, size=12, alpha=0.5, color='green')
    taptool = p.select(type=TapTool)
    taptool.callback = OpenURL(url=url)


# https://docs.bokeh.org/en/latest/docs/user_guide/annotations.html
    return p




