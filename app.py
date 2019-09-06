from flask import Flask
from emoji import demojize
import socket
import logging

app = Flask(__name__)

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'pychat_bot'
token = 'oauth:y1rfxamcdpbprivz59wpmj3dxri3rf'
channel = '#montanablack88'
@app.route('/')
def hello_world():
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s — %(message)s',
                        datefmt='%Y-%m-%d_%H:%M:%S',
                        handlers=[logging.FileHandler(channel+'_chat.log', encoding='utf-8')])

    while True:
        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))

        elif len(resp) > 0:
            logging.info(demojize(resp))


if __name__ == '__main__':
    app.run()
