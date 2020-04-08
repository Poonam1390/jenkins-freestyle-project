from application import app
from flask import request, Response
from random import randint

@app.route('/animal/name', methods=['GET'])
def animanl_name():
    animals = ['duck', 'tiger', 'dog', 'cat']
    return Response(animals[randint(0,3)], mimetype='text/plain')


@app.route('/animal/noise', methods=['POST'])
def animal_noise():
    animal = request.data.decode("utf-8")
    if animal == 'duck':
        noise = 'quak'
    elif animal == 'tiger':
        noise = 'roar'
    elif animal == 'dog':
        noise = 'woof'
    elif animal == 'cat':
        noise = 'meow'
    else:
        noise = 'no noises match the animal you sent'
    return Response(noise, mimetype='text/plain')
