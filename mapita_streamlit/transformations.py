import pandas as pd
import plotly.express as px
import numpy as np


def plot_trap_status(df):
    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        hover_name="ID",
        hover_data=["line"],
        color="color",
        color_discrete_map={"Inactiva": "black", "Activa": "blue", "Captura": "red"},
        height=500,
    )
    fig.update_layout(mapbox_style="open-street-map")
    return fig


def update_trap_lines(original: pd.DataFrame, line):
    merged_df = merge_orginal_line(original, line)
    return add_color(merged_df)


def add_color(expected):
    return expected.assign(
        color=lambda dataframe: dataframe["is_active"].map(
            lambda is_active: "Activa" if is_active else "Inactiva"
        )
    )


def add_captures(original, captures):
    merged = merge_orginal_captures(original, captures)
    merged_with_color = add_color(merged)
    merged_with_color.loc[merged_with_color.captures == True, "color"] = "Captura"
    return merged_with_color


def merge_orginal_line(original: pd.DataFrame, line) -> pd.DataFrame:
    merged_df = original.merge(line, on="line", how="left")
    merged_df["is_active"] = merged_df["is_active_y"].fillna(merged_df["is_active_x"])
    return merged_df


def merge_orginal_captures(original: pd.DataFrame, captures) -> pd.DataFrame:
    merged_df = original.merge(captures, on="ID", how="left")
    return merged_df
