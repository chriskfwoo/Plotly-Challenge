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
models = [item for item in df[df.columns[0]].unique()]
mpg = [item for item in df[df.columns[1]].unique()]


def generate_table(dataframe):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i, _ in enumerate(len(dataframe))]
    )

app.layout = html.Div([
    html.Div([
        html.Div([
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
            x=models,
            y=df[f'{yaxis_column_name}'].values
        )],
        'layout': go.Layout(
            yaxis={
                'title': yaxis_column_name
            }
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)