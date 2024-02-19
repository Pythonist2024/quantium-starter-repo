from dash import Dash, dcc, html 
import pandas as pd 
import plotly.express as px 

df = pd.read_csv("")

df = df.sort_values(by = "date")

app = Dash(__name__)

fig = px.line(df, x = "date", y = "sales", title = "Pink Morsel Sales", color = "region")

app.layout = html.Div([
    html.H1(style = {'textAlign' : 'center'}, children = "Pink Morsel Visualization"),
     
    dcc.Graph(
       id ='Pink Morsel',
       figure = fig
    )
     ])
   
if __name__ == "__main__":
   app.run(debug = True)   
