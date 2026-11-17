from dash import Dash, dcc, html

from src.visualization_project.data.load_data import load_power_plants
from src.visualization_project.visualizations.map_view import create_map
from src.visualization_project.visualizations.scatterplot import create_scatterplot


def create_app():
    app = Dash(__name__, title="Group 14 – Power Plant Explorer")
    try:
        data = load_power_plants()
        status = f"Loaded {len(data):,} power plant records."
        map_figure = create_map(data)
        scatter_figure = create_scatterplot(data)
    except FileNotFoundError as error:
        status = str(error)
        map_figure = create_map(None)
        scatter_figure = create_scatterplot(None)

    app.layout = html.Main([
        html.H1("Global Power Plant Explorer"),
        html.P("Group 14 – JBI100 Visualization"),
        html.P(status),
        html.Div([
            dcc.Graph(id="power-plant-map", figure=map_figure),
            dcc.Graph(id="capacity-generation-scatter", figure=scatter_figure),
        ], style={"display": "grid", "gridTemplateColumns": "repeat(auto-fit, minmax(360px, 1fr))", "gap": "1rem"}),
        html.P("Starter scaffold only: implement the agreed user tasks and linked interactions.")
    ], style={"maxWidth": "1400px", "margin": "2rem auto", "padding": "0 1rem"})
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
