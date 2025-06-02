import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

# Initialize the Dash app


def create_home_layout():
    return html.Div(
        [
            dcc.Location(id="url", refresh=False),
            # Main content
            dbc.Container(
                [
                    dbc.Row(
                        [
                            # Sidebar
                            dbc.Col(
                                [
                                    html.Div(
                                        [
                                            html.H2(
                                                "Telstra", className="sidebar-title"
                                            ),
                                            html.H3(
                                                "CONSUMER MOBILITY FEBRUARY 2025",
                                                className="sidebar-subtitle",
                                            ),
                                            html.P(
                                                [
                                                    "This simulator delivers the key findings for the Consumer Mobility ",
                                                    "conjoint study conducted in February 2025. This study utilises ",
                                                    "novel approaches to choice modelling that reflect behavioural ",
                                                    "economic principles and research findings. The simulator in turn ",
                                                    "accommodates these.",
                                                ],
                                                className="sidebar-text",
                                            ),
                                            html.A(
                                                "ABOUT THE CHOICE MODEL DESIGN",
                                                href="#",
                                                className="about-link",
                                                id="about-link",
                                            ),
                                        ],
                                        className="sidebar-card",
                                    )
                                ],
                                width=3,
                            ),
                            # Main content sections
                            dbc.Col(
                                [
                                    html.Div(
                                        [
                                            html.H2(
                                                "Target Market",
                                                className="section-title",
                                            ),
                                            html.P(
                                                [
                                                    "In the Target Market screen you can select consumer filters for ",
                                                    'the study - press the button "Select Your Target Market" to do this.',
                                                ],
                                                className="section-text",
                                            ),
                                        ],
                                        className="content-card",
                                    ),
                                    html.Div(
                                        [
                                            html.H2(
                                                "Scenario", className="section-title"
                                            ),
                                            html.P(
                                                "Each consumer responds differently to the Scenario settings.",
                                                className="section-text",
                                            ),
                                            html.P(
                                                [
                                                    "This step involves changing various market settings such as; fixed ",
                                                    "product specifications, awareness of features, and brand levers that ",
                                                    "reflect the potential outcome of specific brand and customer ",
                                                    "experience initiatives.",
                                                ],
                                                className="section-text",
                                            ),
                                        ],
                                        className="content-card",
                                    ),
                                    html.Div(
                                        [
                                            html.H2(
                                                "Impact", className="section-title"
                                            ),
                                            html.P(
                                                [
                                                    "After selecting your target market and defining a Scenario, ",
                                                    "here you can review the estimated impact of those changes on ",
                                                    "market share, ARPU and add-on attachments.",
                                                ],
                                                className="section-text",
                                            ),
                                        ],
                                        className="content-card",
                                    ),
                                ],
                                width=6,
                            ),
                            # Action panel
                            dbc.Col(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                dcc.Link(
                                                    "START HERE",
                                                    className="start-btn",
                                                    href="/target-market",
                                                )
                                            ),
                                            html.Button(
                                                "OR EXIT SIMULATOR",
                                                className="exit-btn",
                                                id="exit-btn",
                                            ),
                                        ],
                                        className="action-card",
                                    )
                                ],
                                width=3,
                            ),
                        ]
                    )
                ],
                fluid=True,
                style={"padding": "40px 20px"},
            ),
            # Footer
            html.Div(
                [
                    html.P("Terms & Conditions"),
                    html.P("Sprout Research accepts no liability of any kind"),
                ],
                className="footer-section",
            ),
            html.Div(id="page-content"),
        ]
    )


dash.register_page(
    __name__,
    path="/",
    layout=create_home_layout(),
)
