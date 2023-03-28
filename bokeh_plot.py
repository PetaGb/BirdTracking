from bokeh.models import GMapOptions, ZoomInTool, ZoomOutTool, TapTool, HoverTool, CustomJS
from bokeh.plotting import gmap
import pandas as pd
from main import api_key


bokeh_width, bokeh_height = 1250, 640
df = pd.read_csv("mirabell_2016.csv")
latitudes = df["location_latitude"].values
longitudes = df["location_longitude"].values
date = pd.to_datetime(df["timestamp"]).values


def plot(lat, lng, zoom=5, map_type="roadmap"):
    gmap_options = GMapOptions(lat=lat, lng=lng, map_type=map_type, zoom=zoom)
    p = gmap(api_key, gmap_options, title="2016 the move of Mirabell",
             width=bokeh_width, height=bokeh_height)

    p.add_tools(ZoomInTool(), ZoomOutTool())

    black_triangle(p)
    pink_triangle(p)
    circles(p)

    p.legend.location = "top_left"
    p.legend.title = "Circles legend"
    p.legend.click_policy = "hide"

    return p


def circles(p):
    red = p.circle(longitudes[:180], latitudes[:180], size=7, alpha=0.5, color='red', legend_label="spring move")
    red_hover = HoverTool(tooltips=[("Latitude", "@y"), ("Longitude", "@x"),
                                    ("Date", "@date_time{%Y-%m-%d %H:%M:%S.%3N}")],
                          renderers=[red],
                          formatters={"date_time": "datetime"})

    blue = p.circle(longitudes[180:], latitudes[180:], size=7, alpha=0.5, color="blue", legend_label="autumn move")
    blue_hover = HoverTool(tooltips=[("latitude", "@y"), ("Longitude", "@x")], renderers=[blue])
    p.add_tools(red_hover, blue_hover)

    return red, blue


def black_triangle(p):
    latitude = 47.7352829
    longitude = 8.9074951
    url = "http://127.0.0.1:5000/Radolfzeller_Aachried"
    black_image_path = "https://upload.wikimedia.org/wikipedia/commons/f/f1/White_stork_%28Ciconia_ciconia%29_standing.jpg"
    black = p.triangle(longitude, latitude, size=15, alpha=0.5, color='black', legend_label="interactive black",
                       name="black")
    img_src = f'<img src="{black_image_path}" height="70", width="70">'
    tooltip = f'<div>Latitude: {latitude}<br>Longitude: {longitude}<br>Name: Mirabell<br>URL: {url}<br>{img_src}</div>'
    black_hover = HoverTool(tooltips=tooltip, renderers=[black])
    black_taptool = TapTool(renderers=[black], callback=CustomJS(args=dict(url=url),
                                                                 code="""window.location.replace(url)"""))

    p.add_tools(black_hover, black_taptool)

    return black


def pink_triangle(p):
    latitude = 41.610
    longitude = 0.618
    url = "http://127.0.0.1:5000/Lleida"
    pink_image_path = "https://streetartutopia.com/wp-content/uploads/2021/03/Street-Art-Mural-of-a-stork-nest-by-street-artist-muralist-and-painter-Oriol-Arumi-in-Lleida-Spain-2-1068x1068.jpg"
    pink = p.star(longitude, latitude, size=35, alpha=0.5, color='green', legend_label="interactive pink",
                       name="pink")
    img_src = f'<img src="{pink_image_path}" height="70", width="70">'
    tooltip = f'<div>Latitude: {latitude}<br>Longitude: {longitude}<br>Name: Mural<br>URL: {url}<br>{img_src}</div>'
    pink_hover = HoverTool(tooltips=tooltip, renderers=[pink])
    pink_taptool = TapTool(renderers=[pink],
                            callback=CustomJS(args=dict(url=url), code="""window.location.href = url;"""))

    p.add_tools(pink_hover, pink_taptool)

    return pink
