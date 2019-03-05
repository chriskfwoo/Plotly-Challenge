import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from utils import parse_tsv

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# dataset
df = parse_tsv('mtcars.tsv')

# get the headers from tsv and remove the model header
y_values = list(df)
y_values.remove('model')


# styling dictionaries
flex_center = {
    'display': 'flex',
    'justifyContent': 'center'
}

colors = {
    'grey': '#F4F6F8'
}

def generate_table(dataframe):
    """"
    Generates dash table 

    :param dataframe: dataframe object
    :return: dash table layout
    """

    return html.Div(style=flex_center, children=[html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(len(dataframe))]
    )])

app.layout = html.Div(style={'textAlign': 'center'}, children=[
    html.H1('Motor Trend Car Road Tests'),
    html.Div([
        html.Div(style=flex_center, children=[
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in y_values],
                value='mpg'
            ),
        ])
    ]),
    dcc.Graph(id='bar-graphic'),
    generate_table(df)
])

@app.callback(
    dash.dependencies.Output('bar-graphic', 'figure'),
    [dash.dependencies.Input('yaxis-column', 'value')])
def update_graph(yaxis_column_name):
    return {
        'data': [go.Bar(
            x=[item for item in df[df.columns[0]].unique()],
            y=df[f'{yaxis_column_name}'].values
        )],
        'layout': go.Layout(
                xaxis={
                    'title': 'Models'
                },
                yaxis={
                    'title': yaxis_column_name
                },
                plot_bgcolor=colors['grey']
            ), 
    }

if __name__ == '__main__':
    app.run_server(debug=True)
