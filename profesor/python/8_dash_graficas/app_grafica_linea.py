import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Output, Input
import plotly.express as px

# importarnos los datos de mortalidad
data = pd.read_excel('./data/mortalidad.xlsx')
app = Dash(__name__)

app.layout = html.Div([
    html.H2('Probalidad de fallecimiento en función de la edad'),
    dcc.Store(id='store-data', data=data.to_dict("records")),
    dcc.Graph(id="grafica")
])

@app.callback(
    Output("grafica", 'figure'),
    Input('store-data', "data")
)
def mostrar_grafica(data):
    fig = px.line(
        data,
        x="edad",
        y="qx",
        title='Tabla de mortalidad'
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
