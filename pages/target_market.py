from dash import html, callback, dcc, Output, Input, State
import dash
import dash_bootstrap_components as dbc


def create_target_layout():
    return html.Div(
        [
            dbc.Container(
                [
                    dbc.Row(
                        [
                            # Left side - filters
                            dbc.Col(
                                [
                                    # Stats section
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.H2(
                                                        "3504",
                                                        style={
                                                            "font-size": "2.5rem",
                                                            "font-weight": "bold",
                                                            "color": "#1e293b",
                                                            "margin": "0",
                                                        },
                                                    ),
                                                    html.P(
                                                        "Respondents included (n)",
                                                        style={
                                                            "color": "#64748b",
                                                            "margin": "0",
                                                            "font-size": "0.9rem",
                                                        },
                                                    ),
                                                ],
                                                style={"margin-bottom": "30px"},
                                            ),
                                            html.Div(
                                                [
                                                    html.H2(
                                                        "100%",
                                                        style={
                                                            "font-size": "2.5rem",
                                                            "font-weight": "bold",
                                                            "color": "#1e293b",
                                                            "margin": "0",
                                                        },
                                                    ),
                                                    html.P(
                                                        "% of total weighted active sample",
                                                        style={
                                                            "color": "#64748b",
                                                            "margin": "0",
                                                            "font-size": "0.9rem",
                                                        },
                                                    ),
                                                ],
                                                style={"margin-bottom": "30px"},
                                            ),
                                            # Action buttons
                                        ],
                                        style={"margin-bottom": "40px"},
                                    ),
                                    # Mobile Service Type
                                    html.Div(
                                        [
                                            html.H4(
                                                "Mobile Service Type:",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="mobile-service-type",
                                                options=[
                                                    {
                                                        "label": "Postpaid",
                                                        "value": "postpaid",
                                                    },
                                                    {
                                                        "label": "Pre-paid",
                                                        "value": "prepaid",
                                                    },
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                    # Mobile Broadband
                                    html.Div(
                                        [
                                            html.H4(
                                                "Mobile Broadband:",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="mobile-broadband",
                                                options=[
                                                    {"label": "MBB", "value": "mbb"},
                                                    {
                                                        "label": "No MBB",
                                                        "value": "no_mbb",
                                                    },
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                    # Telstra Customer Status
                                    html.Div(
                                        [
                                            html.H4(
                                                "Telstra Customer Status:",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="telstra-status",
                                                options=[
                                                    {
                                                        "label": "Telstra",
                                                        "value": "telstra",
                                                    },
                                                    {
                                                        "label": "Non-Customer",
                                                        "value": "non_customer",
                                                    },
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                    # Segment
                                    html.Div(
                                        [
                                            html.H4(
                                                "Segment:",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="segment",
                                                options=[
                                                    {
                                                        "label": "Juggling Realists",
                                                        "value": "juggling_realists",
                                                    },
                                                    {
                                                        "label": "Resourceful & Restrained",
                                                        "value": "resourceful_restrained",
                                                    },
                                                    {
                                                        "label": "Prudent & Purposeful",
                                                        "value": "prudent_purposeful",
                                                    },
                                                    {
                                                        "label": "Enthusiastic Compromisers",
                                                        "value": "enthusiastic_compromisers",
                                                    },
                                                    {
                                                        "label": "Energetic & Hyper-attached",
                                                        "value": "energetic_hyper",
                                                    },
                                                    {
                                                        "label": "Ambitious Maximisers",
                                                        "value": "ambitious_maximisers",
                                                    },
                                                    {
                                                        "label": "MBB Warriors",
                                                        "value": "mbb_warriors",
                                                    },
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                    # Generation
                                    html.Div(
                                        [
                                            html.H4(
                                                "Generation:",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="generation",
                                                options=[
                                                    {
                                                        "label": "Gen Z (18-25)",
                                                        "value": "gen_z",
                                                    },
                                                    {
                                                        "label": "Gen Y (26-40)",
                                                        "value": "gen_y",
                                                    },
                                                    {
                                                        "label": "Gen X (41-55)",
                                                        "value": "gen_x",
                                                    },
                                                    {
                                                        "label": "Boomers (56-74)",
                                                        "value": "boomers",
                                                    },
                                                    {
                                                        "label": "Pre-Boomers (75+)",
                                                        "value": "pre_boomers",
                                                    },
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                    # State
                                    html.Div(
                                        [
                                            html.H4(
                                                "State:",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="state",
                                                options=[
                                                    {"label": "NSW", "value": "nsw"},
                                                    {"label": "VIC", "value": "vic"},
                                                    {"label": "QLD", "value": "qld"},
                                                    {"label": "SA", "value": "sa"},
                                                    {"label": "WA", "value": "wa"},
                                                    {"label": "TAS", "value": "tas"},
                                                    {"label": "NT", "value": "nt"},
                                                    {"label": "ACT", "value": "act"},
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                    # Provider
                                    html.Div(
                                        [
                                            html.H4(
                                                "Provider:",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="provider-checklist",
                                                options=[
                                                    {
                                                        "label": "Telstra",
                                                        "value": "Telstra",
                                                    },
                                                    {
                                                        "label": "Optus",
                                                        "value": "Optus",
                                                    },
                                                    {
                                                        "label": "Vodafone",
                                                        "value": "Vodafone",
                                                    },
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                    # Plan Type
                                    html.Div(
                                        [
                                            html.H4(
                                                "Plan Type:",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="plan-type-checklist",
                                                options=[
                                                    {
                                                        "label": "Month to Month",
                                                        "value": "Month to Month",
                                                    },
                                                    {
                                                        "label": "Pre-Paid Cap",
                                                        "value": "Pre-Paid Cap",
                                                    },
                                                    {
                                                        "label": "Pre-Paid Bulk Buy",
                                                        "value": "Pre-Paid Bulk Buy",
                                                    },
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                    # Network Coverage
                                    html.Div(
                                        [
                                            html.H4(
                                                "Network Coverage:",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="network-coverage-checklist",
                                                options=[
                                                    {
                                                        "label": "Full Coverage",
                                                        "value": "Full Coverage",
                                                    },
                                                    {
                                                        "label": "Broad Coverage",
                                                        "value": "Broad Coverage",
                                                    },
                                                    {
                                                        "label": "Partial Coverage",
                                                        "value": "Partial Coverage",
                                                    },
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                    # Monthly Spend
                                    html.Div(
                                        [
                                            html.H4(
                                                "Monthly Spend (Month to Month/Pre-paid Cap):",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="monthly-spend-checklist",
                                                options=[
                                                    {"label": "$10", "value": "$10"},
                                                    {"label": "$25", "value": "$25"},
                                                    {"label": "$50", "value": "$50"},
                                                    {"label": "$80", "value": "$80"},
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                    # Recharge Amount
                                    html.Div(
                                        [
                                            html.H4(
                                                "Recharge Amount (Pre-paid Bulk Buy):",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-weight": "600",
                                                    "margin-bottom": "15px",
                                                },
                                            ),
                                            dcc.Checklist(
                                                id="recharge-amount-checklist",
                                                options=[
                                                    {"label": "$50", "value": "$50"},
                                                    {"label": "$100", "value": "$100"},
                                                    {"label": "$365", "value": "$365"},
                                                ],
                                                value=[],
                                                style={"margin-bottom": "30px"},
                                            ),
                                        ]
                                    ),
                                ],
                                width=8,
                            ),
                            # Right side - info panel and navigation
                            dbc.Col(
                                [
                                    # Navigation buttons
                                    html.Div(
                                        [
                                            dcc.Link(
                                                html.Button(
                                                    "SCENARIO >",
                                                    style={
                                                        "background": "#1e293b",
                                                        "color": "white",
                                                        "border": "none",
                                                        "padding": "15px 30px",
                                                        "font-size": "16px",
                                                        "font-weight": "600",
                                                        "cursor": "pointer",
                                                        "width": "100%",
                                                        "margin-bottom": "20px",
                                                    },
                                                ),
                                                href="/scenario",
                                            ),
                                            dcc.Link(
                                                html.Button(
                                                    "< OR BACK TO HOW TO USE",
                                                    style={
                                                        "background": "transparent",
                                                        "color": "#1e293b",
                                                        "border": "2px solid #e2e8f0",
                                                        "padding": "12px 24px",
                                                        "font-size": "14px",
                                                        "font-weight": "500",
                                                        "cursor": "pointer",
                                                        "width": "100%",
                                                    },
                                                ),
                                                href="/",
                                            ),
                                        ],
                                        style={"margin-bottom": "40px"},
                                    ),
                                    # Info panel
                                    html.Div(
                                        [
                                            html.H3(
                                                "Setting the Target Market",
                                                style={
                                                    "color": "#1e293b",
                                                    "font-size": "1.5rem",
                                                    "font-weight": "600",
                                                    "margin-bottom": "20px",
                                                },
                                            ),
                                            html.P(
                                                [
                                                    "Review the defined consumer groups and decide which groups to include in your scenario. ",
                                                    "Tick the checkbox to include these.",
                                                ],
                                                style={
                                                    "color": "#64748b",
                                                    "line-height": "1.6",
                                                    "margin-bottom": "20px",
                                                },
                                            ),
                                            html.P(
                                                [
                                                    "CHECK NUMBER checks how many consumers you have included."
                                                ],
                                                style={
                                                    "color": "#64748b",
                                                    "line-height": "1.6",
                                                    "margin-bottom": "20px",
                                                },
                                            ),
                                            html.P(
                                                [
                                                    "By default, all consumers are included."
                                                ],
                                                style={
                                                    "color": "#64748b",
                                                    "line-height": "1.6",
                                                    "margin-bottom": "20px",
                                                },
                                            ),
                                            html.P(
                                                [
                                                    "RESET wipes selections and includes all consumers."
                                                ],
                                                style={
                                                    "color": "#64748b",
                                                    "line-height": "1.6",
                                                },
                                            ),
                                        ],
                                        style={
                                            "background": "white",
                                            "padding": "25px",
                                            "border-radius": "12px",
                                            "box-shadow": "0 4px 20px rgba(0, 0, 0, 0.1)",
                                        },
                                    ),
                                ],
                                width=4,
                            ),
                        ]
                    )
                ],
                fluid=True,
                style={"padding": "20px"},
            ),
            # dcc.Store stores the intermediate value
            dcc.Store(
                id="target_market_data_value",
                storage_type="local",  # Use 'local' storage to persist data across sessions
            ),
            dcc.Store(id="callback_execution_tracker", data={"has_run": False}),
        ]
    )


# Callbacks for button clicks
dash.register_page(
    __name__,
    path="/target-market",
    layout=create_target_layout(),
)


@callback(
    Output("submit-button", "n_clicks"),
    Input("submit-button", "n_clicks"),
    State("target_market_data_value", "data"),  # Read data from target_market_data
    prevent_initial_call=True,
)
def print_target_market_data(n_clicks, target_market_data):
    print("Intermediate Value:", target_market_data)  # Print the stored value
    return n_clicks


@callback(
    Output("target_market_data_value", "data"),
    [
        Input("mobile-service-type", "value"),
        Input("mobile-broadband", "value"),
        Input("telstra-status", "value"),
        Input("segment", "value"),
        Input("generation", "value"),
        Input("state", "value"),
        Input("provider-checklist", "value"),
        Input("plan-type-checklist", "value"),
        Input("network-coverage-checklist", "value"),
        Input("monthly-spend-checklist", "value"),
        Input("recharge-amount-checklist", "value"),
    ],
    prevent_initial_call=True,
)
def update_target_market_data(
    mobile_service_type,
    mobile_broadband,
    telstra_status,
    segment,
    generation,
    state,
    provider,
    plan_type,
    network_coverage,
    monthly_spend,
    recharge_amount,
):

    target_market_data = {
        "mobile_service_type": mobile_service_type,
        "mobile_broadband": mobile_broadband,
        "telstra_status": telstra_status,
        "segment": segment,
        "generation": generation,
        "state": state,
        "provider": provider,
        "plan_type": plan_type,
        "network_coverage": network_coverage,
        "monthly_spend": monthly_spend,
        "recharge_amount": recharge_amount,
    }
    print("Updating Target Market Data with Values:", target_market_data)
    return target_market_data


@callback(
    [
        Output("mobile-service-type", "value"),
        Output("mobile-broadband", "value"),
        Output("telstra-status", "value"),
        Output("segment", "value"),
        Output("generation", "value"),
        Output("state", "value"),
        Output("provider-checklist", "value"),
        Output("plan-type-checklist", "value"),
        Output("network-coverage-checklist", "value"),
        Output("monthly-spend-checklist", "value"),
        Output("recharge-amount-checklist", "value"),
    ],
    Input("target_market_data_value", "data"),
    prevent_initial_call=False,
)
def prefill_checkboxes(target_market_data):
    print("Prefill Checkboxes with Data:", target_market_data)
    if target_market_data:
        return (
            target_market_data.get("mobile_service_type", []),
            target_market_data.get("mobile_broadband", []),
            target_market_data.get("telstra_status", []),
            target_market_data.get("segment", []),
            target_market_data.get("generation", []),
            target_market_data.get("state", []),
            target_market_data.get("provider", []),
            target_market_data.get("plan_type", []),
            target_market_data.get("network_coverage", []),
            target_market_data.get("monthly_spend", []),
            target_market_data.get("recharge_amount", []),
        )
    return ([], [], [], [], [], [], [], [], [], [], [])
