from dash import html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px
from django_plotly_dash import DjangoDash
import os
from ...functions.feat_ext import fe_data
from ...functions.db_connect import return_df
import dash
from textwrap import dedent

table = return_df()
df = fe_data(table)


app = DjangoDash('SimpleExample',add_bootstrap_links=True)
app.css.append_css({ "external_url" : "/static/assets/s1.css" })

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Colors
bgcolor = "#f3f3f1"  # mapbox light map land color
bar_bgcolor = "#b0bec5"  # material blue-gray 200
bar_unselected_color = "#78909c"  # material blue-gray 400
bar_color = "#546e7a"  # material blue-gray 600
bar_selected_color = "#37474f"  # material blue-gray 800
bar_unselected_opacity = 0.8


# Figure template
row_heights = [150, 500, 300]
template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}


def blank_fig(height):
    """
    Build blank figure with the requested height
    """
    return {
        "data": [],
        "layout": {
            "height": height,
            "template": template,
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
        },
    }


def build_modal_info_overlay(id, side, content):
    """
    Build div representing the info overlay for a plot panel
    """
    div = html.Div(
        [  # modal div
            html.Div(
                [  # content div
                    html.Div(
                        [
                            html.H4(
                                [
                                    "Info",
                                    html.Img(
                                        id=f"close-{id}-modal",
                                        src="/static/assets/times-circle-solid.svg",
                                        n_clicks=0,
                                        className="info-icon",
                                        style={"margin": 0},
                                    ),
                                ],
                                className="container_title",
                                style={"color": "white"},
                            ),
                            dcc.Markdown(content),
                        ]
                    )
                ],
                className=f"modal-content {side}",
            ),
            html.Div(className="modal"),
        ],
        id=f"{id}-modal",
        style={"display": "none"},
    )

    return div




"""
Dash Layout
"""


elements = ['Views','Likes','Comments','DurationinSeconds']

app.layout = html.Div(
    children=[
        html.Div(
            [
                html.H1(
                    children=[
                        "S Sport Youtube Channel Dashboard",
                        html.A(
                            html.Img(
                                src="/static/assets/icon.png",
                                style={"float": "right", "height": "50px"},
                            ),
                            href="https://dash.plot.ly/",
                        ),
                    ],
                    style={"text-align": "left"},
                ),
            ]
        ),
        html.Div(
            children=[
                build_modal_info_overlay(
                    "subscriberInfo",
                    "top",
                    dedent(
                        """
            Total Subscriber S Sport has
            """
                    ),
                ),
                build_modal_info_overlay(
                    "videosInfo",
                    "top",
                    dedent(
                        """
            Total Videos S Sport uploaded
        """
                    ),
                ),
                build_modal_info_overlay(
                    "viewsInfo",
                    "top",
                    dedent(
                        """
            Total views S Sport has
        """
                    ),
                ),
                build_modal_info_overlay(
                    "scatterInfo",
                    "top",
                    dedent(
                        """
            The _**Signal Range**_ panel displays a histogram of the signal range of
            each tower in the dataset.  The dark gray bars represent the set of towers
            in the current selection, while the light gray bars underneath represent
            all towers in the dataset.

            Left-click drag to select histogram bars using the box-selection tool.

            The _**Clear Selection**_ button may be used to clear any selections
            applied in the _**Signal Range**_ panel, while leaving any selections
            applied in other panels unchanged.
        """
                    ),
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Subscribers",
                                        html.Img(
                                            id="show-subscriberInfo-modal",
                                            src="/static/assets/question-circle-solid.svg",
                                            n_clicks=0,
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                dcc.Loading(
                                    dcc.Graph(
                                        id="subscriberInfo-graph",
                                        figure=blank_fig(row_heights[0]),
                                        config={"displayModeBar": False},
                                    ),
                                    className="svg-container",
                                    style={"height": 150},
                                ),
                                html.Div(
                                    children=[
                                        html.Button(
                                            "Reset All",
                                            id="subscriberInfo-clear-all",
                                            className="reset-button",
                                        ),
                                    ]
                                ),
                            ],
                            className="four columns pretty_container",
                            id="subscriberInfo-div",
                        ),
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Videos",
                                        html.Img(
                                            id="show-videosInfo-modal",
                                            src="/static/assets/question-circle-solid.svg",
                                            n_clicks=0,
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                dcc.Loading(
                                    dcc.Graph(
                                        id="videosInfo-graph",
                                        figure=blank_fig(row_heights[0]),
                                        config={"displayModeBar": False},
                                    ),
                                    className="svg-container",
                                    style={"height": 150},
                                ),
                                html.Div(
                                    children=[
                                        html.Button(
                                            "Reset All",
                                            id="videosInfo-clear-all",
                                            className="reset-button",
                                        ),
                                    ]
                                ),
                            ],
                            className="four columns pretty_container",
                            id="videosInfo-div",
                        ),
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Views",
                                        html.Img(
                                            id="show-viewsInfo-modal",
                                            src="/static/assets/question-circle-solid.svg",
                                            n_clicks=0,
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                dcc.Loading(
                                    dcc.Graph(
                                        id="vieswInfo-graph",
                                        figure=blank_fig(row_heights[0]),
                                        config={"displayModeBar": False},
                                    ),
                                    className="svg-container",
                                    style={"height": 150},
                                ),
                                html.Div(
                                    children=[
                                        html.Button(
                                            "Reset All",
                                            id="viewsInfo-clear-all",
                                            className="reset-button",
                                        ),
                                    ]
                                ),
                            ],
                            className="four columns pretty_container",
                            id="viewsInfo-div",
                        ),
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Videos by Categories",
                                        html.Img(
                                            id="show-scatterInfo-modal",
                                            src="/static/assets/question-circle-solid.svg",
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                dcc.Graph(
                                    id="scatterInfo-graph",
                                    figure=blank_fig(row_heights[1]),
                                    config={"displayModeBar": False},
                                ),
                                dcc.RangeSlider(
                                    id='range-slider',
                                    min=2018, max=2023, step=1,
                                    marks={2018:'2018', 2019:'2019', 2020:'2020', 2021:'2021', 2022:'2022', 2023: '2023'},
                                    value=[2018, 2023]
                                    ),
                                dcc.Dropdown(
                                    elements,
                                    'Likes',
                                    id='xaxis-column',
                                ),
                                dcc.Dropdown(
                                    elements,
                                    'Views',
                                    id='yaxis-column'
                                )
                            ],
                            className="twelve columns pretty_container",
                            style={
                                "width": "98%",
                                "margin-right": "0",
                            },
                            id="scatterInfo-div",
                    ),
                                    ]
                ),
            ]
        ),
        html.Div(
            [
                html.H4("Acknowledgements", style={"margin-top": "0"}),
                dcc.Markdown(
                    """\
 - Dashboard written in Python using the [Dash](https://dash.plot.ly/) web framework.
 - Parallel and distributed calculations implemented using the [Dask](https://dask.org/) Python library.
 - Server-side visualization of the location of all 40 million cell towers performed
 using the [Datashader] Python library (https://datashader.org/).
 - Base map layer is the ["light" map style](https://www.mapbox.com/maps/light-dark/)
 provided by [mapbox](https://www.mapbox.com/).
 - Cell tower dataset provided by the [OpenCelliD Project](https://opencellid.org/) which is licensed under a
[_Creative Commons Attribution-ShareAlike 4.0 International License_](https://creativecommons.org/licenses/by-sa/4.0/).
 - Mapping from cell MCC/MNC to network operator scraped from https://cellidfinder.com/mcc-mnc.
 - Icons provided by [Font Awesome](https://fontawesome.com/) and used under the
[_Font Awesome Free License_](https://fontawesome.com/license/free).
"""
                ),
            ],
            style={
                "width": "98%",
                "margin-right": "0",
                "padding": "10px",
            },
            className="twelve columns pretty_container",
        ),
    ]
)




for id in ["subscriberInfo", "videosInfo", "viewsInfo", "scatterInfo"]:

    @app.callback(
        [Output(f"{id}-modal", "style"), Output(f"{id}-div", "style")],
        [Input(f"show-{id}-modal", "n_clicks"), Input(f"close-{id}-modal", "n_clicks")],
    )
    def toggle_modal(n_show, n_close):
        ctx = dash.callback_context
        if ctx.triggered and ctx.triggered[0]["prop_id"].startswith("show-"):
            return {"display": "block"}, {"zIndex": 1003}
        else:
            return {"display": "none"}, {"zIndex": 0}




@app.callback(
    Output('scatterInfo-graph', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input("range-slider", "value"))
def update_graph(xaxis_column_name, yaxis_column_name, slider_range):

    low, high = slider_range
    #mask = (df['Year'] >= low) & (df['Year'] < high)

    fig = px.scatter(df,x=xaxis_column_name,
            y=yaxis_column_name,
            hover_name='Title',
            color='Categories'
            )

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig



