import csv
import os
import sys

CLIENT_SCHEMA = ['name', 'lastname', 'email', 'phone']
CLIENT_TABLE = 'clients.csv'
clients = []

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('El cliente ya se encuentra registrado')

def list_clients():
    print('Id |  Nombres  | Apellidos  | Correo  | Telefono ')
    print('-' * 50)

    for idx, client in enumerate(clients):
        print('{id} | {name} | {lastname} | {email} | {phone}'.format(
            id=idx, 
            name=client['name'], 
            lastname=client['lastname'], 
            email=client['email'], 
            phone=client['phone']))

def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('El cliente no se encuentra registrado')

def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break

def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

def _get_client_field(field_name, message='{} ?'):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field

def _get_client_from_user():
    client = {
        'name': _get_client_field('Sus nombres'),
        'lastname': _get_client_field('Sus apellidos'),
        'email': _get_client_field('Su correo'),
        'phone': _get_client_field('Su telefono'),
    }
    return client

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)
    f.close()

def _save_clients_to_storage():
    with open(CLIENT_TABLE, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

def _print_welcome():
    print('BIENVENIDOS AL ADMINISTRADOR DE CLIENTES')
    print('-' * 50)
    print('[C]rear cliente')
    print('[L]istar clientes')
    print('[A]ctualizar cliente')
    print('[E]liminar cliente')
    print('[B]uscar cliente')
    print('[S]alir')    
    print('')
    print('Seleccione una opción: ')

if __name__ == '__main__':
    _initialize_clients_from_storage()

    while(True):
        _print_welcome()

        command = input()
        command = command.upper()

        if command == 'C':
            client = _get_client_from_user()
            create_client(client)
            _save_clients_to_storage()
        elif command == 'L':
            list_clients()
        elif command == 'A':
            client_id = int(_get_client_field('id'))
            updated_client = _get_client_from_user()
            update_client(client_id, updated_client)
            _save_clients_to_storage()
        elif command == 'E':
            client_id = int(_get_client_field('id'))
            delete_client(client_id)
            _save_clients_to_storage()
        elif command == 'S':
            sys.exit()
        elif command == 'B':
            client_name = _get_client_field('name')
            found = search_client(client_name)
            
            if found:
                print('El cliente ya se encuentra registrado')
            else:
                print('The cliente: {} no se encuentra registrado '.format(client_name))
        else:
            print('Opción invalida')

    
