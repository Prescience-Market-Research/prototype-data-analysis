import dash
from dash import Dash, html, dcc
from external_stylesheets import external_stylesheets
from index_string import index_string
import dash_bootstrap_components as dbc
from header import create_header


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.MINTY],
    suppress_callback_exceptions=True,
    use_pages=True,
)

app.index_string = index_string

app.layout = html.Div(
    [
        create_header(),
        dash.page_container,
    ]
)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)
