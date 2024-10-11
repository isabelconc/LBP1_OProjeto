# models.py

users = {
    "admin": "password123"
}

def check_login(username, password):
    return users.get(username) == password

def register_user(username, password):
    if username in users:
        return False  # Usuário já existe
    users[username] = password
    return True  # Registro bem-sucedido
