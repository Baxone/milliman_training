
def get_clients_by_tramo(clients_list, tramo): 56


def get_total_caidas(clients_list):
    contador = 0
    for client in clients_list:
        if client['vigor'] == False:
            contador += 1
    return contador


def percent_global(clients_list):
    total = len(clients_list)  # 20polizas
    total_caidas = get_total_caidas(clients_list)
    print(f"{(total_caidas / total ) * 100}%")


def get_data():
    # en esta función en futuro podriamos por ejemplo extraer un excel, csv o consultar BBDD
    return [
        {'id': 1, 'name': 'Juan', 'age': 43, 'vigor': True},
        {'id': 2, 'name': 'María', 'age': 29, 'vigor': False},
        {'id': 3, 'name': 'Luis', 'age': 34, 'vigor': True},
        {'id': 4, 'name': 'Ana', 'age': 22, 'vigor': False},
        {'id': 5, 'name': 'Carlos', 'age': 55, 'vigor': True},
        {'id': 6, 'name': 'Marta', 'age': 31, 'vigor': True},
        {'id': 7, 'name': 'Pedro', 'age': 40, 'vigor': True},
        {'id': 8, 'name': 'Lucía', 'age': 27, 'vigor': False},
        {'id': 9, 'name': 'José', 'age': 60, 'vigor': True},
        {'id': 10, 'name': 'Elena', 'age': 45, 'vigor': False},
        {'id': 11, 'name': 'Miguel', 'age': 38, 'vigor': True},
        {'id': 12, 'name': 'Isabel', 'age': 52, 'vigor': False},
        {'id': 13, 'name': 'Andrés', 'age': 47, 'vigor': True},
        {'id': 14, 'name': 'Rosa', 'age': 58, 'vigor': False},
        {'id': 15, 'name': 'Javier', 'age': 33, 'vigor': True},
        {'id': 16, 'name': 'Sandra', 'age': 26, 'vigor': True},
        {'id': 17, 'name': 'Alberto', 'age': 49, 'vigor': True},
        {'id': 18, 'name': 'Paula', 'age': 30, 'vigor': False},
        {'id': 19, 'name': 'Fernando', 'age': 41, 'vigor': True},
        {'id': 20, 'name': 'Laura', 'age': 24, 'vigor': False},
    ]
