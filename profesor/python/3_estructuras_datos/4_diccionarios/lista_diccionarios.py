clientes = [
    {'id': 1, 'name': 'Juan', 'genero': 'm',
        'capital_bruto': '35000', 'age': 30, 'q_ext': 0.2},
    {'id': 2, 'name': 'Maria', 'genero': 'f',
        'capital_bruto': '40000', 'age': 23, 'q_ext': 0.1},
    {'id': 3, 'name': 'Pedro', 'genero': 'm',
        'capital_bruto': '52000', 'age': 27, 'q_ext': 0.15},
    {'id': 4, 'name': 'Lucia', 'genero': 'f',
        'capital_bruto': '46000', 'age': 32, 'q_ext': 0.3},
    {'id': 5, 'name': 'Ana', 'genero': 'f',
        'capital_bruto': '38000', 'age': 28, 'q_ext': 0.05},
    {'id': 6, 'name': 'Carlos', 'genero': 'm',
        'capital_bruto': '60000', 'age': 40, 'q_ext': 0.25},
    {'id': 7, 'name': 'Luis', 'genero': 'm',
        'capital_bruto': '42000', 'age': 35, 'q_ext': 0.12},
    {'id': 8, 'name': 'Sofia', 'genero': 'f',
        'capital_bruto': '33000', 'age': 22, 'q_ext': 0.08},
    {'id': 9, 'name': 'Elena', 'genero': 'f',
        'capital_bruto': '55000', 'age': 29, 'q_ext': 0.18},
    {'id': 10, 'name': 'Miguel', 'genero': 'm',
        'capital_bruto': '48000', 'age': 31, 'q_ext': 0.22}
]

# intentar que lo que hagais os sirve para otros porcentajes

# opcion 1: Junior


def get_clients_by_qext(list, qext_min, qext_max):
    clients_filter = []
    for client in list:
        if client['q_ext'] >= qext_min and client['q_ext'] <= qext_max:
            clients_filter.append(client)
    return clients_filter


clients_0_10 = get_clients_by_qext(clientes, 0, 0.10)
clients_10_20 = get_clients_by_qext(clientes, 0.1, 0.20)
print(clients_10_20)


# opcion 2: Senior
def get_clients_by_qext_2(client_list, qext_min, qext_max):
    return list(filter(
        lambda client: client['q_ext'] >= qext_min and client['q_ext'] <= qext_max, client_list))


clients_10_20_2 = get_clients_by_qext_2(clientes, 0.1, 0.20)
print(clients_10_20_2)

# obtener clientes con mas de 30 años y un riesgo por encima de 30 - 100

print('----------------------------------------------')
# opcion 1: Junior


def get_clients_by_age(clients_list, agemin):
    clients_filter = []
    for client in clients_list:
        if client['age'] >= agemin:
            clients_filter.append(client)
    return clients_filter


def get_clients_by_age_2(clients_list, agemin):
    return list(filter(lambda client: client['age'] >= agemin, clients_list))


clients_30_1 = get_clients_by_age(clientes, 30)
clients_30_2 = get_clients_by_age_2(clientes, 30)
clients_30_30_100 = get_clients_by_qext_2(clients_30_2, 0.3, 1)
print(clients_30_30_100)
