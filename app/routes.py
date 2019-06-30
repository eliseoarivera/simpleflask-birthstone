from flask import render_template, request, redirect
from app import app
from app.models import model, formopener
from app.models.formopener import dict_from
#from app.models.model import birthMonth

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method == 'GET':
        return "Please use form"
    else:
        userdata = dict_from(request.form)
        print(userdata)
        birthMonth = userdata['birthMonth']
        birthMonth = model.birthStone(birthMonth)
        return render_template('results.html', birthMonth = birthMonth)
    