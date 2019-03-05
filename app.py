import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from utils import parse_tsv

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = parse_tsv()
y_values = list(df)
y_values.remove('model')

dropdown_style = {
    'display': 'flex',
    'justifyContent': 'center'
}

table_style = {
    'display': 'flex',
    'justifyContent': 'center'
}

def generate_table(dataframe):
    return html.Div(style=table_style, children=[html.Table(
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
        html.Div(style=dropdown_style, children=[
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
                yaxis={
                    'title': yaxis_column_name
                },
            ), 
    }

if __name__ == '__main__':
    app.run_server(debug=True)
