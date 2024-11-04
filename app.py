from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
# db_config = {
#     'host': 'localhost',
#     'user': 'flask_user',
#     'password': 'flask_password',
#     'database': 'flask_app_db'
# }
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1967188',
    'database': 'Tarea_Flask'
}

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route('/add_user', methods=['POST'])
def add_user():
    # Obtener los datos enviados en la solicitud
    name = request.form.get('NOMBRE')
    email = request.form.get('CORREO')

    # Insertar los datos en la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Usuarios (NOMBRE, CORREO) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Usuario agregado con éxito!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
