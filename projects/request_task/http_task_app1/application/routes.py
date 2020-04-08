import requests
from flask import render_template, redirect, url_for, request
from application import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='HomePage')


@app.route('/get/animal', methods=['GET', 'POST'])
def animals():
    api = "http://http_task_app2:5001"
    animal = requests.get(api + '/animal/name')
    noise = requests.post(api + '/animal/noise',data=animal.text)
    return render_template('animals.html',title='Animals', animal= animal.text, noise=noise.text)
