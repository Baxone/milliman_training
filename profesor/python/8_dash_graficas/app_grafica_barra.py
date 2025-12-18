import pandas as pd
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc

# importarnos los datos de mortalidad
data = pd.read_csv('./data/cartera.csv')
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
## themes de bootrap

# asegurarnos que prima_anual sea numericad
data['prima_anual'] = pd.to_numeric(data['prima_anual'], errors='coerce')

## agrupación por producto - suma de prima anual por producto
tabla_resumen = ( data.dropna(subset=['producto', 'prima_anual'])
                 .groupby("producto", as_index=False)['prima_anual'].sum()
                 .sort_values("prima_anual", ascending=False)
                 )

fig = px.bar(
    tabla_resumen,
    x='producto',
    y='prima_anual',
    title="Suma de prima anual por producto",
    template='plotly_dark'
)
fig.update_layout(xaxis_title="Producto", yaxis_title="Prima anual total")


app.layout = dbc.Container(fluid=True, children=[
    #Fila
    dbc.Row([
        # Primera columna
        dbc.Col(html.Div(style={"height": "100vh"}, children=[
            html.H2('Grafica de barras'),
            dbc.Button('Grafica de barras', id="btn-grafica" ,className='btn btn-warn me-3'),
            dbc.Button('Tabla',id="btn-tabla", className='btn btn-warning')
            ]), width=3),
         #Segunda columna
        dbc.Col(children=[
            dbc.Container(
                dcc.Graph(figure=fig, id='grafica', style={"display":"block"})
            ),
            dbc.Container(
                html.Div(id='contenedor-tabla', style={'display':'none'}, children=[
                        dash_table.DataTable(
                            data=tabla_resumen.to_dict('records'),
                            columns=[{'name': col, 'id':col} for col in tabla_resumen.columns],
                            page_size=10,
                            filter_action="native",
                            style_cell={
                                "backgroundColor": "#1b1b1b"
                            }        
                            )   
                ]), className='p-3'
            )
            ], width=9)
    ]),
    # Otra fila
    dbc.Row([
        
    ])
])

@app.callback(
    Output('grafica', 'style'),
    Output('contenedor-tabla', 'style'),
    Input('btn-tabla', 'n_clicks'),
    Input('btn-grafica', 'n_clicks')
)
def mostrar_tabla(n_tabla, n_grafica):
    # por defecto grafica esta visible
    if (n_tabla or 0) > (n_grafica or 0):
        return {'display': 'none'},  {'display': 'block'}
    
    return {'display': 'block'},  {'display': 'none'}   

if __name__ == "__main__":
    app.run(debug=True)
