from users.user import User
from notes.notes import Note

options = """
    1.- Crear usuarios
    2.- Buscar usuario
    3.- Eliminar usuario
    4.- Actualizar usuario
    5.- Crear nota
    6.- Salir
"""


def menu():
    print(options)
    option_selected = int(input())
    function_to_execute = get_function_to_execute(option_selected)
    function_to_execute()


def get_function_to_execute(option_selected):
    select_options = {
        1: create_user,
        2: get_user_by_id,
        3: delete_user_by_id,
        4: update_user_by_id,
        5: create_note,
        6: exit
    }
    return select_options.get(option_selected)


def create_user():
    name = input("Ingresa tu nombre: ")
    last_name = input("Ingresa tu apellido: ")
    age = int(input("Ingresa tu edad: "))
    email = input("Ingresa tu email: ")
    user = User(
        name=name,
        last_name=last_name,
        age=age,
        email=email,
    )
    print(user.create())

def get_user_by_id():
    user_id = input("Ingrese su id: ")
    print(User.get_user_by_id(user_id=user_id))

def delete_user_by_id():
    user_id = input("Ingrese su id: ")
    print(User.delete_user(user_id=user_id))

def update_user_by_id():
    user_id = input("Ingrese su id: ")
    name = input("Ingresa tu nombre: ")
    last_name = input("Ingresa tu apellido: ")
    age = int(input("Ingresa tu edad: "))
    email = input("Ingresa tu email: ")
    new_data_user = {
        'name': name, 'last_name': last_name,
        'age': age, 'email': email
    }
    print(User.update_user(user_id=user_id, data=new_data_user))

def create_note():
    user_id = input("Ingrese su id: ")
    content = input("Ingrese el contenido de su nota: ")

    note = Note(
        user_id=user_id,
        content=content
    )
    print(note.create())
