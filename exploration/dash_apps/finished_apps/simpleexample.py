from dash import html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px
from django_plotly_dash import DjangoDash
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv('video_data_04-11-22.csv')


app.layout = dash_table.DataTable(df.to_dict('records'), 
[{"name": i, "id": i} for i in df.columns],
page_size=10)


