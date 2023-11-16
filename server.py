from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app, ping_timeout=20, ping_interval=10) 

@app.route('/')
def index():
    return render_template('index.html')




@socketio.on('message')
def handle_message(message):
    if isinstance(message, bytes):
        decoded_message = message.decode('utf-8')
    else:
        decoded_message = message
    print(f"Received message: {decoded_message}")
    print(type(decoded_message))
    socketio.emit('message', decoded_message)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == "__main__":
    socketio.run(app, debug=True)