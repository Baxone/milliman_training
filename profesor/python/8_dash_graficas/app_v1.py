from dash import Dash, html

# Crear la app
app = Dash(__name__)

# Definir un pequeño interfaz
app.layout = html.Div([
    html.H1("Mi primera aplicacion con dash"),
    html.P("Esta pintando un interfaz en python")
])

# arrancar el servidor
if __name__ == "__main__":
    app.run(debug=True)