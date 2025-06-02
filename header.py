from dash import dcc, html, Input, Output, callback


def create_header():
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Link(
                                "How to use simulator",
                                className="nav-step",
                                href="/",
                            ),
                            dcc.Link(
                                "1 - Target Market",
                                className="nav-step active",
                                href="/target-market",
                            ),
                            dcc.Link(
                                "2 - Scenario",
                                className="nav-step",
                                href="/scenario",
                            ),
                            dcc.Link(
                                "3 - Impact",
                                className="nav-step",
                                href="/impact",
                            ),
                        ],
                        style={"display": "flex", "gap": "5px"},
                    ),
                ],
                style={
                    "max-width": "1200px",
                    "margin": "0 auto",
                    "display": "flex",
                    "justify-content": "space-between",
                    "align-items": "center",
                    "padding": "0 20px",
                    "flex-wrap": "wrap",
                    "gap": "20px",
                },
            )
        ],
        className="header-gradient",
    )
