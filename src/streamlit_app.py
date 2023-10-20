import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px

path_geojson = "tests/data/traps_03SEP2023.geojson"
with open(path_geojson, encoding="utf8") as json_traps:
    traps = json.load(json_traps)

lat = [feature["properties"]["lat"] for feature in traps["features"]]
lon = [feature["properties"]["lon"] for feature in traps["features"]]
id = [feature["properties"]["ID"] for feature in traps["features"]]
line = [feature["properties"]["line"] for feature in traps["features"]]
colour = [
    "Activa" if feature["properties"]["is_active"] else "Inactiva" for feature in traps["features"]
]


df = pd.DataFrame({"lat": lat, "lon": lon, "color": colour, "ID": id, "line": line})

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    hover_name="ID",
    hover_data=["line"],
    color="color",
    color_discrete_map={"Inactiva": "black", "Activa": "blue"},
    height=500,
)
fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig)
