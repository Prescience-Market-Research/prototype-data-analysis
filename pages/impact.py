from typing import OrderedDict
import pandas as pd
from dash import html
import dash
from dash_ag_grid import AgGrid
import dash_ag_grid as dag
from dash import Dash, Input, Output, html, dcc, callback
from plotly import data

df_per_row_dropdown = pd.DataFrame(
    OrderedDict(
        [
            ("City", ["NYC", "Montreal", "Los Angeles"]),
            ("Neighborhood", ["Brooklyn", "Mile End", "Venice"]),
            ("Temperature (F)", [70, 60, 90]),
        ]
    )
)


def create_layout():
    return html.Div(
        [
            html.H1("Impact Market"),
            html.P("Content for Target Market will go here."),
            # Add more content as needed
            # AgGrid(
            #     id="dropdown_per_row",
            #     rowData=df_per_row_dropdown.to_dict("records"),
            #     columnDefs=[
            #         {"field": "City"},
            #         {
            #             "field": "Neighborhood",
            #             "editable": True,
            #             "cellRenderer": "StockLink",
            #             "cellEditorParams": {
            #                 "values": {
            #                     "NYC": ["Brooklyn", "Queens", "Staten Island"],
            #                     "Montreal": ["Mile End", "Plateau", "Hochelaga"],
            #                     "Los Angeles": ["Venice", "Hollywood", "Los Feliz"],
            #                 },
            #             },
            #         },
            #         {"field": "Temperature (F)"},
            #     ],
            # ),
            html.Button("Download CSV", id="csv-button", n_clicks=0),
            AgGrid(
                csvExportParams={
                    "fileName": "ag_grid_test.csv",
                },
                id="option_component_grid",
                rowData=[
                    {"City": "NYC", "Option": "Option 1"},
                    {"City": "Montreal", "Option": "Option 2"},
                    {"City": "Los Angeles", "Option": "Option 3"},
                ],
                columnDefs=[
                    {"field": "City"},
                    {
                        "field": "Option",
                        "cellRenderer": "OptionComponent",
                        "editable": True,
                        "cellRendererParams": {
                            "options": [
                                {"label": "Option 1", "value": "Option 1"},
                                {"label": "Option 2", "value": "Option 2"},
                                {"label": "Option 3", "value": "Option 3"},
                            ],
                        },
                    },
                ],
            ),
        ]
    )


@callback(
    Output("option_component_grid", "exportDataAsCsv"),
    Input("csv-button", "n_clicks"),
)
def export_data_as_csv(n_clicks):
    if n_clicks:
        return True
    return False


dash.register_page(
    __name__,
    path="/impact",
    layout=create_layout(),
)
