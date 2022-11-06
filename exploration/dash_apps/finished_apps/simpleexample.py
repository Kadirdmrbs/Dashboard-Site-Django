from dash import html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px
from django_plotly_dash import DjangoDash
import os
from ...functions.feat_ext import fe_data
from ...functions.db_connect import return_df

table = return_df()
df = fe_data(table)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

table = df[['Id','Title','Date','Comments','Likes','Views','DurationinSeconds','Categories','SubCategory']]

app.layout = dash_table.DataTable(df.to_dict('records'), 
[{"name": i, "id": i} for i in table.columns],
page_size=10)


