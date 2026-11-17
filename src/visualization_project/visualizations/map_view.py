import plotly.express as px
import plotly.graph_objects as go


def create_map(data):
    if data is None or data.empty:
        return go.Figure().update_layout(title="Power plant locations (dataset not loaded)")
    valid = data.dropna(subset=["latitude", "longitude"])
    fig = px.scatter_mapbox(
        valid, lat="latitude", lon="longitude",
        color="primary_fuel" if "primary_fuel" in valid else None,
        size="capacity_mw" if "capacity_mw" in valid else None,
        hover_name="name" if "name" in valid else None,
        hover_data=[c for c in ["country", "primary_fuel", "capacity_mw"] if c in valid],
        zoom=1, height=600,
    )
    fig.update_layout(mapbox_style="open-street-map", margin={"r": 0, "t": 35, "l": 0, "b": 0})
    return fig
