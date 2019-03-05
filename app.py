import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import parse_tsv

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def generate_table(dataframe, max_rows=30):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

app.layout = html.Div(children=[
    html.H4(children='Motor Trend Car Road Tests'),
    generate_table(parse_tsv())
])

if __name__ == '__main__':
    app.run_server(debug=True)
