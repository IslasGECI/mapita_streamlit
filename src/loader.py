import streamlit as st
import pandas as pd
import json

from mapita_streamlit import add_color, plot_trap_status, update_trap_lines


traps_file = st.file_uploader("Choose a GeoJSON")
captures_file = st.file_uploader("Choose a csv")

if captures_file is not None:
    captures_df = pd.read_csv(captures_file)
    st.write(captures_df)


if traps_file is not None:
    traps = json.load(traps_file)

    lat = [feature["properties"]["lat"] for feature in traps["features"]]
    lon = [feature["properties"]["lon"] for feature in traps["features"]]
    id = [feature["properties"]["ID"] for feature in traps["features"]]
    line = [feature["properties"]["line"] for feature in traps["features"]]
    is_active = [feature["properties"]["is_active"] for feature in traps["features"]]

    df = pd.DataFrame({"lat": lat, "lon": lon, "ID": id, "line": line, "is_active": is_active})
    df = add_color(df)

    lines_df = pd.DataFrame({"line": ["Linea Cerco", "Linea 1"], "is_active": [False, False]})

    edited_df = st.data_editor(lines_df, hide_index=True)

    map_df = update_trap_lines(df, edited_df)

    fig = plot_trap_status(map_df)
    st.plotly_chart(fig)

    st.write("Made with 💖 by GECI")
