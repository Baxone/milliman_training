from dash import Dash, html, dcc
#necesitamos esta libreria para poder introducir datos guardarlos temporalmente Input
# necesitamos pintar datos Outputs
from dash.dependencies import Input, Output

app = Dash(__name__)


app.layout = html.Div([
    html.H2('Calcula de prima simple'),
    html.Label('Edad'),
    dcc.Input(id='edad', type='number'),
    html.Label('Capital Asegurado'),
    dcc.Input(id='capital', type='number'),
    html.Br(),
    # linea grafica horizontal para separar visuales.
    html.Div(id='resultado') 
])

@app.callback(
    Output("resultado", "children" ),
    Input("edad", "value"),
    Input("capital", "value"),
)
def calcular_prima(edad, capital):
    if edad is None:
        return "Introduce una edad valida"
    
    if capital is None:
        return "Introduce un capital valido"
    
    prima = edad * capital 
    return f"La prima anual estimada es {prima} €"

if __name__ == "__main__":
    app.run(debug=True)