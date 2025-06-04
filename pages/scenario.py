from dash import html, dcc, callback, Output, Input, State
import dash
import pandas as pd
from .helpers.transform_product_specifications import transform_product_specifications
import plotly.express as px
from dash_ag_grid import AgGrid


# Read the CSV file
product_specifications = pd.read_csv("data/product-specification.csv")
responses_data = pd.read_csv("data/responses.csv")


scenario_reflected_data_final = transform_product_specifications(product_specifications)


def create_layout():
    return html.Div(
        [
            html.H1("Scenario Market"),
            html.P("Selected target market"),
            html.Div(id="target-market-data-display"),
            html.H2("Product Specification"),
            html.Button("Download CSV Display", id="csv-button", n_clicks=0),
            AgGrid(
                id="scenario_grid",
                rowData=product_specifications.to_dict("records"),
                columnDefs=[
                    (
                        {
                            "field": col,
                            "cellRenderer": "OptionComponent",
                            "editable": True,
                            "cellRendererParams": {
                                "options": [
                                    {"label": "Telstra", "value": "Telstra"},
                                    {"label": "Optus", "value": "Optus"},
                                    {"label": "Vodafone", "value": "Vodafone"},
                                    {"label": "TPG", "value": "TPG"},
                                    {"label": "Other", "value": "Other"},
                                ],
                            },
                        }
                        if col == "Provider"
                        else {"field": col}
                    )
                    for col in product_specifications.columns
                ],
                defaultColDef={"editable": True},
            ),
            html.Div(style={"height": "50px"}),  # Adds a gap between sections
            html.H2("Responses"),
            AgGrid(
                id="responses_grid",
                rowData=responses_data.to_dict("records"),
                columnDefs=[
                    {
                        "headerName": "Provider",
                        "children": [
                            {"field": "Telstra"},
                            {"field": "Optus"},
                            {"field": "Vodafone"},
                        ],
                    },
                    {
                        "headerName": "Plan Type",
                        "children": [
                            {"field": "Month to Month"},
                            {"field": "Pre-Paid Cap"},
                            {"field": "Pre-Paid Bulk Buy"},
                        ],
                    },
                    {
                        "headerName": "Network Coverage",
                        "children": [
                            {"field": "Full Coverage"},
                            {"field": "Broad Coverage"},
                            {"field": "Partial Coverage"},
                        ],
                    },
                    {
                        "headerName": "Monthly Spend",
                        "children": [
                            {"field": "$10"},
                            {"field": "$25"},
                            {"field": "$50"},
                            {"field": "$80"},
                        ],
                    },
                    {
                        "headerName": "Recharge Amount",
                        "children": [
                            {"field": "$50"},
                            {"field": "$100"},
                            {"field": "$365"},
                        ],
                    },
                ],
                defaultColDef={"editable": True},
            ),
            html.Div(style={"height": "50px"}),  # Adds a gap between sections
            html.H2("Reflected Scenario Grid"),
            html.Button(
                "Download CSV Real Value", id="csv-real-value-button", n_clicks=0
            ),
            AgGrid(
                id="scenario_reflected_grid",
                rowData=scenario_reflected_data_final.to_dict("records"),
                columnDefs=[
                    {"field": "On/Off"},
                    {"field": "Product"},
                    {
                        "headerName": "Provider",
                        "children": [
                            {"field": "Telstra"},
                            {"field": "Optus"},
                            {"field": "Vodafone"},
                        ],
                    },
                    {
                        "headerName": "Plan Type",
                        "children": [
                            {"field": "Month to Month"},
                            {"field": "Pre-Paid Cap"},
                            {"field": "Pre-Paid Bulk Buy"},
                        ],
                    },
                    {
                        "headerName": "Network Coverage",
                        "children": [
                            {"field": "Full Coverage"},
                            {"field": "Broad Coverage"},
                            {"field": "Partial Coverage"},
                        ],
                    },
                    {
                        "field": "Minimum Monthly Spend",
                    },
                ],
            ),
            dcc.Store(
                id="target_market_data_value",
                storage_type="local",
            ),
            dcc.Store(id="updated_input_data", storage_type="local"),
        ]
    )


dash.register_page(
    __name__,
    path="/scenario",
    layout=create_layout(),
)


@callback(
    Output("scenario_grid", "exportDataAsCsv"),
    Input("csv-button", "n_clicks"),
)
def export_data_as_csv(n_clicks):
    if n_clicks:
        return True
    return False


@callback(
    Output("scenario_reflected_grid", "exportDataAsCsv"),
    Input("csv-real-value-button", "n_clicks"),
)
def export_data_as_csv(n_clicks):
    if n_clicks:
        return True
    return False


@callback(
    Output("target-market-data-display", "children"),
    Input("target_market_data_value", "data"),
)
def display_target_market_data(target_market_data_value):
    print("Target market data value received:", target_market_data_value)
    return html.Pre(f"Target market data value: {target_market_data_value}")


@callback(
    Output("updated_input_data", "data"),
    Input("input-data-table", "data"),
)
def save_updated_table_to_store(updated_data):
    # Save the updated table data to the store
    return updated_data


@callback(
    Output("scenario_reflected_grid", "rowData"),
    Input("scenario_grid", "cellValueChanged"),
    State("scenario_grid", "rowData"),
)
def update_scenario_reflected_grid(_, _scenario_grid_data):
    print("Callback triggered with data222:", _scenario_grid_data)
    # Convert _scenario_grid_data to a pandas DataFrame
    scenario_grid_df = pd.DataFrame(_scenario_grid_data)

    # Transform the DataFrame
    reflected_data = transform_product_specifications(scenario_grid_df)
    # Convert the transformed DataFrame back to a list of dictionaries for rowData
    return reflected_data.to_dict("records")
