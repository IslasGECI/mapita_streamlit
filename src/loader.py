import streamlit as st
import pandas as pd
import json
import plotly.express as px

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    traps = json.load(uploaded_file)

    lat = [feature["properties"]["lat"] for feature in traps["features"]]
    lon = [feature["properties"]["lon"] for feature in traps["features"]]
    id = [feature["properties"]["ID"] for feature in traps["features"]]
    line = [feature["properties"]["line"] for feature in traps["features"]]
    colour = [
        "Activa" if feature["properties"]["is_active"] else "Inactiva" for feature in traps["features"]
    ]
    is_active = [feature["properties"]["is_active"] for feature in traps["features"]]


    df = pd.DataFrame({"lat": lat, "lon": lon, "color": colour, "ID": id, "line": line, "is_active": is_active})
    
    lines_df = pd.DataFrame({"line": ["Linea Cerco", "Linea 1"], "is_active": [False, False]})
    
    edited_df = st.data_editor(lines_df, hide_index=True)
    
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

