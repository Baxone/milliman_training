import pandas as pd
from dash import Dash, html, dcc, dash_table
#necesitamos esta libreria para poder introducir datos guardarlos temporalmente Input
# necesitamos pintar datos Outputs
from dash.dependencies import Input, Output

# leemos el csv con pandas y lo cargamos en df
df = pd.read_csv('./data/cartera.csv')

# para ordenar por fecha convierto el campos fecha en fecha real
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'], errors="coerce")
app = Dash(__name__)

app.layout = html.Div(
    style={"maxWidth": "1100px", "margin":"30px 20px", "fontFamily": "Arial", "color":"#0D72DE"},
    children=[
        html.H2('Cartera de polizas - Tabla filtrable'),
        dash_table.DataTable(
            id="tabla_polizas",
            columns=[{'name':i, 'id': i} for i in df.columns],
            data=df.to_dict("records"),
            
            # filtros por columna
            filter_action="native",
            
            # ordenar por columnas
            sort_action="native",
            sort_mode="multi",
            
            #paginacion
            page_action="native",
            page_size=10,
            
            style_cell = { 'padding': '10px', 'textAlign':'left' }
        )
    ]
    )


if __name__ == "__main__":
    app.run(debug=True)