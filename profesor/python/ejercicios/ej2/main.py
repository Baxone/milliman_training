from lib.poliza import Poliza


def main():
    menu = """Analisis de polizas
[1]. Calcular prima media
[2]. Calcular suma total asegurada
[3]. Calcular edad media
[4]. Filtrar poliza por cabecera
[5]. Calcular valor presente de la prima
[x]. Salir del programa
     """
    print(menu)
    option = input('Selecciona una opción: ')
    poliza = Poliza('cartera_polizas', 'csv')
    if option == '1':
        # calcular prima media
        cabecera = input('Dime que sobre cabecera quieres calcular: ')
        results = poliza.promedio(cabecera)
        print(f"{results:.5f}")
    elif option == '2':
        # calcular suma total asegurada
        results = poliza.sumatorio('suma_asegurada')
        formatted = f"{results:,.5f}"
        # Swap separators: commas (thousands) -> dots, dot (decimal) -> comma
        formatted = formatted.replace(',', 'X').replace(
            '.', ',').replace('X', '.')
        print(f"{formatted} €")
    elif option == '3':
        # calcular edad media
        try:
            cabecera = input('dime el campo a buscar: ')
            results = poliza.promedio(cabecera)
            print(f"{results:.2f}")
        except KeyError:
            print('La cabecera solicita no esta disponible')
            main()
    elif option == '4':
        cabecera = input('Dime el campo sobre el que filtrar: ')
        min = float(input('Dame el valor minimo sobre el que filtrar: '))
        max = float(input('Dame el valor máximo: '))
        df = poliza.filter_by_head(cabecera, min, max)
        print(df)
    elif option == '5':
        numero_anios = int(input('Dame el numero de años para calcular: '))
        tasa = int(input('Dame la tasa: '))
        for i in range(numero_anios, 0, -1):
            df = poliza.get_present_value(tasa, i)
            print(df.head())
    elif option == 'x':
        print('Hasta pronto')
    else:
        print('Opción no valida')
        main()


if __name__ == '__main__':
    main()
