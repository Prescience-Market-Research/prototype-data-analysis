from dash import html, dcc, callback, Output, Input, State
import dash
import pandas as pd
import plotly.express as px
from dash_ag_grid import AgGrid


# Read the CSV file
product_specifications = pd.read_csv("data/product-specification.csv")
responses_data = pd.read_csv("data/responses.csv")

# Create a new DataFrame reflecting the values of scenario_grid
# 1. get the header of the responses_data
headers = responses_data.columns.tolist()
product_specifications_config = [
    {
        "field": "Provider",
        "children": [
            {"field": "Telstra"},
            {"field": "Optus"},
            {"field": "Vodafone"},
        ],
    },
    {
        "field": "Plan Type",
        "children": [
            {"field": "Month to Month"},
            {"field": "Pre-Paid Cap"},
            {"field": "Pre-Paid Bulk Buy"},
        ],
    },
    {
        "field": "Network Coverage",
        "children": [
            {"field": "Full Coverage"},
            {"field": "Broad Coverage"},
            {"field": "Partial Coverage"},
        ],
    },
    {
        "field": "Monthly Spend",
        "children": [
            {"field": "$10"},
            {"field": "$25"},
            {"field": "$50"},
            {"field": "$80"},
        ],
    },
    {
        "field": "Recharge Amount",
        "children": [
            {"field": "$50"},
            {"field": "$100"},
            {"field": "$365"},
        ],
    },
]
print("Header of responses_data:", headers)
# scenario_reflected_data = pd.DataFrame(columns=header)
scenario_reflected_data = pd.DataFrame(
    columns=headers,
    data=[],
)
# loop though each item in product_specifications_config
# and create a new column in scenario_reflected_data that has all the children of the item
# field is the column name of the product_specifications
for item in product_specifications_config:
    product_specifications_column_name = item["field"]
    children = item["children"]
    for child in children:
        responses_data_column_name = child["field"]
        product_specifications_col = product_specifications[
            product_specifications_column_name
        ]
        scenario_reflected_data[responses_data_column_name] = (
            product_specifications_col.apply(
                lambda x: 1 if pd.notna(x) and x != "" else 0
            )
        )

    # scenario_reflected_data[col] = product_specifications[col].apply(lambda x: 1 if pd.notna(x) and x != "" else 0)
# 2. the value of the product_specifications is the header of the responses_data
# 3. if the cell has a value, set the value to 1, otherwise set it to 0
# scenario_reflected_data = pd.DataFrame(
#     columns=responses_data.columns,
#     data=[
#         {
#             col: 1 if product_specifications[col].any() else 0
#             for col in responses_data.columns
#         }
#         for _ in range(len(product_specifications))
#     ],
# )
print("Scenario reflected data created with columns:", scenario_reflected_data.columns)


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
            AgGrid(
                id="scenario_reflected_grid",
                rowData=scenario_reflected_data.to_dict("records"),
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
    Input("scenario_grid", "rowData"),
)
def update_scenario_reflected_grid(scenario_grid_data):
    if scenario_grid_data:
        # Convert the data: if a cell has a value, set it to 1; otherwise, set it to 0
        reflected_data = [
            {key: 1 if value else 0 for key, value in row.items()}
            for row in scenario_grid_data
        ]
        return reflected_data
    return []
