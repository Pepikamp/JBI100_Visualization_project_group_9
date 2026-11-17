import plotly.express as px
import plotly.graph_objects as go


def create_scatterplot(data):
    if data is None or data.empty:
        return go.Figure().update_layout(title="Capacity vs generation (dataset not loaded)")
    y_candidates = ["estimated_generation_gwh_2017", "generation_gwh_2017", "generation_gwh_2016"]
    y = next((column for column in y_candidates if column in data), None)
    if "capacity_mw" not in data or y is None:
        return go.Figure().update_layout(title="Required capacity/generation columns not found")
    valid = data.dropna(subset=["capacity_mw", y])
    return px.scatter(
        valid, x="capacity_mw", y=y,
        color="primary_fuel" if "primary_fuel" in valid else None,
        hover_name="name" if "name" in valid else None,
        labels={"capacity_mw": "Installed capacity (MW)", y: f"{y.replace('_', ' ')} (GWh)"},
        title="Installed capacity vs electricity generation",
    )
