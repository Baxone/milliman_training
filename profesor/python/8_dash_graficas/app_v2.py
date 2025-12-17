from dash import Dash, html, dcc

app = Dash(__name__)


app.layout = html.Div([
    html.H2('Entrada de datos de edad en mi aplicación'), 
    html.Label('Introduce la edad'),
    dcc.Input(id="edad", type="number", value=30)
])


if __name__ == "__main__":
    app.run(debug=True)