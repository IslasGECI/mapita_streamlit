import streamlit as st
import pandas as pd
import json

from mapita_streamlit import add_color, plot_trap_status

path_geojson = "tests/data/traps_03SEP2023.geojson"
with open(path_geojson, encoding="utf8") as json_traps:
    traps = json.load(json_traps)

lat = [feature["properties"]["lat"] for feature in traps["features"]]
lon = [feature["properties"]["lon"] for feature in traps["features"]]
id = [feature["properties"]["ID"] for feature in traps["features"]]
line = [feature["properties"]["line"] for feature in traps["features"]]
is_active = [feature["properties"]["is_active"] for feature in traps["features"]]

df = pd.DataFrame({"lat": lat, "lon": lon, "ID": id, "line": line, "is_active": is_active})
df = add_color(df)


fig = plot_trap_status(df)
st.plotly_chart(fig)
