from dash import html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px
from django_plotly_dash import DjangoDash
import os
from ...functions.featen import fe_data


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv('../../functions/video_data_04-11-22.csv')

new_df = fe_data(df)
table = new_df[['Id','Title','Date','Comments','Likes','Views','DurationinSeconds','Categories','SubCategory']]

app.layout = dash_table.DataTable(new_df.to_dict('records'), 
[{"name": i, "id": i} for i in table.columns],
page_size=10)


