def main():
    menu = """## Elige un frase para hoy ##
[1] - Me van a subir el sueldo
[2] - Va ser un buen día
[3] - En el gimnasio voy a darlo todo
[4] - Hasta mañana
"""
    print(menu)
    option = input('Selecciona una opcion: ')
    if option == '1':
        print('Te han subido el sueldo 300 euros al mes')
    elif option == '2':
        print('Hoy tienes el guapo subido')
    elif option == '3':
        print('hoy levantas 140 en press banca')
    elif option == '4':
        print('hasta pronto, vuelve cuando quieras')
    else:
        print('opción no permitida, selecciona otra: ')
        main()


main()
