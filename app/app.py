from flask_socketio import SocketIO, emit, join_room, leave_room
import eventlet
from flask import Flask, request
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/", methods=['GET'])
def hello():
    return "Welcome server socket"

@socketio.on('connect')
def test_connect():
    print('someone connected to websocket')
    emit('responseMessage', {'data': 'nuevo usuario conectado'}, broadcast=True)


@socketio.on('message', namespace='/devices')
def handle_message2():
    print('someone sent to the websocket!')


# si ocurre un error en el socket
@socketio.on_error_default
def default_error_handler(e):
    print('An error occured:')
    print(e)


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')