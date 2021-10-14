from flask import Flask, request, json
from settings import *
import vk
import messageHandler
app = Flask(__name__)

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
    return 'ok'

@app.route('/')
def hello_world():
    return 'https://oauth.vk.com/authorize?client_id=7417919&edirect_uri=https://oauth.vk.com/blank.html&display=page&scope=friends,photos,audio,status,video,wall,offline,groups,notify,docs&response_type=token&v=5.50'
