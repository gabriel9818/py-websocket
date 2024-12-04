from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('mensaje')
def handle_message(data):
    nombre = data.get('nombre', 'Desconocido')  # Si no envían nombre, usa 'Desconocido'
    mensaje = f"Hola {nombre}!"
    socketio.emit('respuesta', {'mensaje': mensaje})

if __name__ == '__main__':
    socketio.run(app)
