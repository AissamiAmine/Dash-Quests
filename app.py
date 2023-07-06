import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


url = 'https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv'
df = pd.read_csv(url, on_bad_lines='skip')

# Créer Dash
app = dash.Dash(__name__)

#  le graphique 
fig = px.scatter(df, x='average_rating', y='ratings_count', hover_data=['title'])

# Définir la mise en page de l'application
app.layout = html.Div([
    dcc.Graph(id='graph', figure=fig),
    html.Label('Variable 1'),
    dcc.Dropdown(
        id='variable1',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='average_rating'
    ),
    html.Label('Variable 2'),
    dcc.Dropdown(
        id='variable2',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='ratings_count'
    ),
])

# Définir les callbacks
@app.callback(
    Output('graph', 'figure'),
    Input('variable1', 'value'),
    Input('variable2', 'value')
)
def update_graph(variable1, variable2):
    fig = px.scatter(df, x=variable1, y=variable2, hover_data=['title'])
    return fig

# Lancer l'application Dash
if __name__ == '__main__':
    from pyngrok import ngrok

    # Exposer l'application sur un lien externe
    app.run_server(mode='external')

