import socketio

server_url = "http://localhost:5000"  # Update this with your server URL
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('message')
def on_message(data):
    print('Message from server:', data)

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

sio.connect(server_url)

try:
    while True:
        message = input("Enter a message to send to the server (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        sio.emit('message', message)
except KeyboardInterrupt:
    pass
finally:
    sio.disconnect()
