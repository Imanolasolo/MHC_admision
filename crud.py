import sqlite3
import bcrypt
import jwt  # Importar el módulo JWT

# Clave secreta para firmar los tokens JWT
SECRET_KEY = "tu_clave_secreta"  # ¡Cambia esto por una clave segura en un entorno de producción!

def generate_token(dni, role):
    payload = {
        'dni': dni,
        'role': role
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def create_user(dni, username, password, role):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # Busca el nombre del rol en lugar del ID
        c.execute('SELECT role_name FROM roles WHERE id = ?', (role,))
        role_name = c.fetchone()
        if role_name:
            user_id = generate_token(dni, role_name[0])  # Genera el token JWT como ID
            c.execute('INSERT INTO users (id, dni, username, password, role) VALUES (?, ?, ?, ?, ?)', 
                      (user_id, dni, username, hashed_password.decode('utf-8'), role_name[0]))
            conn.commit()
            return True
        else:
            return False
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def read_users():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('''
        SELECT users.id, users.dni, users.username, users.role
        FROM users
    ''')
    users = c.fetchall()
    conn.close()
    return users


def update_user(user_id, dni, username, password, role):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        c.execute('UPDATE users SET dni = ?, username = ?, password = ?, role = ? WHERE id = ?', 
                  (dni, username, hashed_password.decode('utf-8'), role, user_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating user: {e}")
    finally:
        conn.close()

def delete_user(user_id):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    try:
        c.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")
    finally:
        conn.close()

def create_role(role_name, permissions):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO roles (role_name, permissions) VALUES (?, ?)', (role_name, permissions))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error creating role: {e}")
        return False
    finally:
        conn.close()

def read_roles():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('SELECT * FROM roles')
    roles = c.fetchall()
    conn.close()
    return roles

def update_role(role_id, role_name, permissions):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    try:
        c.execute('UPDATE roles SET role_name = ?, permissions = ? WHERE id = ?', (role_name, permissions, role_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating role: {e}")
    finally:
        conn.close()

def delete_role(role_id):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    try:
        c.execute('DELETE FROM roles WHERE id = ?', (role_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting role: {e}")
    finally:
        conn.close()



