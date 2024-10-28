import bcrypt

# Simulación de un hash almacenado en la base de datos
stored_hash = b'$2b$12$IipvE5zl5CLpS0hN4R2WyergzWvIszwZT5etAvwzTAuWdAmV7LX/e'

# Contraseña ingresada por el usuario (debe coincidir con la original)
password = 'Ilargietaeguzki1'

# Verificar la contraseña ingresada con el hash almacenado
if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
    print("Contraseña válida")
else:
    print("Contraseña inválida")
