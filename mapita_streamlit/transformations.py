import pandas as pd
import plotly.express as px


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
    pass


def merge_orginal_line(original: pd.DataFrame, line) -> pd.DataFrame:
    merged_df = original.merge(line, on="line", how="left")
    merged_df["is_active"] = merged_df["is_active_y"].fillna(merged_df["is_active_x"])
    return merged_df
